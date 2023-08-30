from django.db import models

from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from wagtail.search import index
from wagtail.signals import page_published
from wagtail.snippets.models import register_snippet

from home.blocks import *
# Create your models here.

class PersonPage(Page):
    template = "team/team_detail.html"

    parent_page_types = ["PersonIndexPage"]

    role = models.CharField(max_length=255, blank=True)
    is_senior = models.BooleanField(default=False)
    intro = RichTextField(blank=True)
    biography = RichTextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    call_to_action = StreamField(
        PageSectionStoryBlock(),
        blank=True,
        use_json_field=True,
        collapsed=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("biography"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("role"),
        FieldPanel("is_senior"),
        FieldPanel("intro"),
        FieldPanel("biography"),
        FieldPanel("image"),
        FieldPanel("call_to_action"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

    @cached_property
    def author_posts(self):
        # return the blogs writen by this member
        author_snippet = Author.objects.get(person_page__pk=self.pk)

        # format for template
        return [
            {
                "title": blog_post.title,
                "url": blog_post.url,
                "author": blog_post.first_author,
                "date": blog_post.date,
            }
            for blog_post in BlogPage.objects.live()
            .filter(authors__author=author_snippet)
            .order_by("-date")
        ]

    @cached_property
    def related_works(self):
        # Get the latest 2 work pages by this author
        works = (
            WorkPage.objects.filter(authors__author__person_page=self.pk)
            .live()
            .public()
            .distinct()
            .order_by("-date")[:2]
        )
        return works

    @cached_property
    def work_index(self):
        return WorkIndexPage.objects.live().public().first()


# Person index
class PersonIndexPage(Page):
    strapline = models.CharField(max_length=255)
    call_to_action = StreamField(
        PageSectionStoryBlock(),
        blank=True,
        use_json_field=True,
        collapsed=True,
    )

    template = "team/team_listing.html"

    subpage_types = ["PersonPage"]

    @cached_property
    def team(self):
        return PersonPage.objects.order_by("-is_senior", "title").live().public()

    content_panels = Page.content_panels + [
        FieldPanel("strapline"),
        FieldPanel("call_to_action"),
    ]

# An author snippet which keeps a copy of a person's details in case they leave and their page is unpublished
# Could also be used for external authors
@register_snippet
class Author(index.Indexed, models.Model):
    person_page = models.OneToOneField(
        "partners.PersonPage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def update_manual_fields(self, person_page):
        self.name = person_page.title
        self.role = person_page.role
        self.image = person_page.image

    def clean(self):
        if not self.person_page and not self.name:
            raise ValidationError(
                {"person_page": "You must set either 'Person page' or 'Name'"}
            )

        if self.person_page:
            self.update_manual_fields(self.person_page)

    def __str__(self):
        return self.name

    search_fields = [
        index.SearchField("name"),
    ]

    panels = [
        FieldPanel("person_page"),
        MultiFieldPanel(
            [FieldPanel("name"), FieldPanel("role"), FieldPanel("image")],
            "Manual fields",
        ),
    ]