from django.db import models
from django.contrib.auth import get_user_model

from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from wagtail.search import index
from wagtail.signals import page_published
from wagtail.snippets.models import register_snippet

from home.blocks import *
# Create your models here.

User = get_user_model()

# An author snippet which keeps a copy of a person's details in case they leave and their page is unpublished
# Could also be used for external authors
@register_snippet
class Author(index.Indexed, models.Model):
    #user = models.OneToOneField(User, null=True, blank=True,on_delete=models.SET_NULL, related_name="+",)
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def update_manual_fields(self, user):
        self.name = user.title
        self.role = user.role
        self.image = user.image

    def clean(self):
        if not self.user and not self.name:
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
        MultiFieldPanel(
            [FieldPanel("name"), FieldPanel("role"), FieldPanel("image")],
            "Manual fields",
        ),
    ]
