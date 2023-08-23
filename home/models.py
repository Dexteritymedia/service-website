from django.db import models
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel )
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from .blocks import *

class HomePage(Page):
    template = "homepage.html"
    max_count = 1

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
    template = 'service.html'
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

        context['services'] = services
        return context


class StaticPage(Page):
    template = 'static_detail.html'
    parent_page_types = [
        'HomePage'
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
    

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)

class FormPage(AbstractEmailForm):

    template = 'contact_page.html'

    subpage_types = [
        #app_name.model,
        'home.FormPage',
    ]
    parent_page_types = [
        'HomePage'
        ]
    show_in_menus_default = True
    
    max_count = 2
    
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    use_other_template = models.BooleanField(null=True, blank=True, default='No', verbose_name='New Template', help_text='Use a different template',)

    def get_template(self, request, *args, **kwargs):
        if self.use_other_template:
            return 'testimonial_page.html'
        return 'contact_page.html'


    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('use_other_template'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('intro', classname='full'),
        FieldPanel('thank_you_text', classname='full'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        testimonials = FormPage.objects.live().public().order_by('-first_published_at')[:5]

        context['testimonials'] = testimonials
        return context


