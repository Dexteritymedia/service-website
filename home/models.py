import json
from os.path import splitext

from django.db import models
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import format_html
from django.urls import reverse

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel )
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, FORM_FIELD_CHOICES
from wagtail.models import Collection
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.views import SubmissionsListView
from wagtail.images import get_image_model
from wagtail.images.fields import WagtailImageField
from wagtail.contrib.forms.panels import FormSubmissionsPanel

from .blocks import *

class HomePage(Page):
    template = "homepage.html"
    max_count = 1
    parent_page_types = [
        'HomePage'
        ]

    show_in_menus_default = True

    content = StreamField(HomePageBlock(), use_json_field=True, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
    

class Service(Page):
    max_count = 1
    template = 'services.html'
    parent_page_types = [
        'HomePage'
        ]

    show_in_menus_default = True
    
    call_to_action = StreamField(
        PageSectionStoryBlock(),
        blank=True,
        use_json_field=True,
        collapsed=False,
        null=True,
    )
    body = StreamField(StoryBlock(), use_json_field=True, blank=True, null=True)


    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("call_to_action"),
    ]


    def get_context(self, request):
        context = super().get_context(request)
        all_services = ServicePage.objects.live().public().order_by('-first_published_at')
        

        paginator = Paginator(all_services, 20)

        page = request.GET.get('page')
        try:
            services = paginator.page(page)
        except PageNotAnInteger:
            services = paginator.page(1)
        except EmptyPage:
            services = paginator.page(paginator.num_pages)

        context['services'] = services
        return context
        
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

        
class ServicePage(Page):

    template = 'service_details.html'
    parent_page_types = [
        'Service'
        ]

    service_title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    other_services_title = models.CharField(max_length=100, default='Services We also Offer')

    images = StreamField(
        [
            ('photos', PhotoGridBlock()),
        ],

        blank=True,
        use_json_field=True,
        null=True

    )

    show_in_menus_default = True
    

    content_panels = Page.content_panels + [
        FieldPanel('service_title'),
        FieldPanel('description'),
        FieldPanel('images'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('other_services_title'),
    ]


    class Meta:
        verbose_name = 'Service detail'
        verbose_name_plural = 'Service details'


    def get_context(self, request):
        context = super().get_context(request)
        services = ServicePage.objects.live().public().exclude(id=self.id).order_by('-first_published_at')[:4]
        service = Service.objects.live().public()

        context['service'] = service
        context['services'] = services
        return context


class StaticPage(Page):
    template = 'static_detail.html'
    parent_page_types = [
        'HomePage'
        ]
    subpage_types = [
        'StaticPage'
        ]
    page_description = "Use this page to create an about page, terms and condition page"
    
    call_to_action = StreamField(
        PageSectionStoryBlock(),
        blank=True,
        use_json_field=True,
        collapsed=False,
        null=True,
    )
    
    body = StreamField(StoryBlock(), use_json_field=True, null=True)

    show_in_menus_default = True

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("call_to_action"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("call_to_action"),
    ]
        
    
    class Meta:
        verbose_name = 'Other Page'
        verbose_name_plural = 'Other Pages'

    def get_context(self, request):
        context = super().get_context(request)
        service = Service.objects.live().public()

        context['service'] = service
        return context


class CustomFormBuilder(FormBuilder):

    def create_image_field(self, field, options):
        return WagtailImageField(**options)


class CustomSubmissionsListView(SubmissionsListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.is_export:

            # generate a list of field types, the first being the injected 'submission date'
            field_types = ['submission_date'] + [field.field_type for field in self.form_page.get_form_fields()]
            data_rows = context['data_rows']
            ImageModel = get_image_model()

            for data_row in data_rows:

                fields = data_row['fields']

                for idx, (value, field_type) in enumerate(zip(fields, field_types)):
                    if field_type == 'image' and value:
                        image = ImageModel.objects.get(pk=value)
                        rendition = image.get_rendition('fill-100x75|jpegquality-40')
                        preview_url = rendition.url
                        url = reverse('wagtailimages:edit', args=(image.id,))
                        # build up a link to the image, using the image title & id
                        fields[idx] = format_html(
                            "<a href='{}'><img alt='Uploaded image - {}' src='{}' />{} ({})</a>",
                            url,
                            image.title,
                            preview_url,
                            image.title,
                            value
                        )

        return context
    

class FormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        choices=list(FORM_FIELD_CHOICES) + [('image', 'Upload Image')]
    )
    
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)

class FormPage(AbstractEmailForm):

    template = 'contact_page.html'

    form_builder = CustomFormBuilder
    submissions_list_view_class = CustomSubmissionsListView

    subpage_types = [
        #app_name.model,
        'home.FormPage',
    ]
    parent_page_types = [
        'HomePage'
        ]
    show_in_menus_default = True
    
    max_count = 2
    
    text = RichTextField(blank=True)
    landing_page_text = RichTextField(blank=True)
    use_other_template = models.BooleanField(default=False, blank=True, verbose_name='New Page Template', help_text='Use a different template',)
    uploaded_image_collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def get_template(self, request, *args, **kwargs):
        if self.use_other_template:
            return 'registration_page.html'
        return 'contact_page.html'


    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('text', classname='full'),
        FieldPanel('use_other_template'),
        FieldPanel('uploaded_image_collection'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('landing_page_text', classname='full'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        testimonials = FormPage.objects.live().public().order_by('-first_published_at')[:5]

        context['testimonials'] = testimonials
        return context


    def get_uploaded_image_collection(self):
        """
        Returns a Wagtail Collection, using this form's saved value if present,
        otherwise returns the 'Root' Collection.
        """
        collection = self.uploaded_image_collection

        return collection or Collection.get_first_root_node()

    @staticmethod
    def get_image_title(filename):
        """
        Generates a usable title from the filename of an image upload.
        Note: The filename will be provided as a 'path/to/file.jpg'
        """

        if filename:
            result = splitext(filename)[0]
            result = result.replace('-', ' ').replace('_', ' ')
            return result.title()
        return ''

    def process_form_submission(self, form):
        """
        Processes the form submission, if an Image upload is found, pull out the
        files data, create an actual Wgtail Image and reference its ID only in the
        stored form response.
        """

        cleaned_data = form.cleaned_data

        for name, field in form.fields.items():
            if isinstance(field, WagtailImageField):
                image_file_data = cleaned_data[name]
                if image_file_data:
                    ImageModel = get_image_model()

                    kwargs = {
                        'file': cleaned_data[name],
                        'title': self.get_image_title(cleaned_data[name].name),
                        'collection': self.get_uploaded_image_collection(),
                    }

                    if form.user and not form.user.is_anonymous:
                        kwargs['uploaded_by_user'] = form.user

                    image = ImageModel(**kwargs)
                    image.save()
                    # saving the image id
                    # alternatively we can store a path to the image via image.get_rendition
                    cleaned_data.update({name: image.pk})
                else:
                    # remove the value from the data
                    del cleaned_data[name]

        submission = self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
        )

        # important: if extending AbstractEmailForm, email logic must be re-added here
        # if self.to_address:
        #    self.send_mail(form)

        return submission

