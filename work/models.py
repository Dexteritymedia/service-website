import math
import string

from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.dispatch import receiver
from django.shortcuts import render
from django.utils.decorators import method_decorator

from bs4 import BeautifulSoup
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from wagtail.signals import page_published
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.users.models import UserProfile

from home.blocks import *


class WorkPageScreenshot(Orderable):
    page = ParentalKey("work.WorkPage", related_name="screenshots")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("image"),
    ]


class WorkPage(RoutablePageMixin, Page):
    template = "work/work_detail.html"

    parent_page_types = ["WorkIndexPage"]
    subpage_types = [
        'work.WorkPage',
    ]

    body = StreamField(StoryBlock(), use_json_field=True)
    

    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        help_text="Image used on listings and social media.",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def get_context(self, request):
        context = super().get_context(request)
        author_details = WorkPage.objects.get(id=self.id)
        author_works = WorkPage.objects.filter(owner=self.owner).live().public().order_by('-first_published_at').exclude(pk=self.pk)[:4]
        author_page = UserProfile.objects.get(user=self.owner)
        print(author_page)

        context['author_works'] = author_works
        context['author_details'] = author_details
        context['author_page'] = author_page
        return context

    @path('author/')
    def author_works(self, request,):
        all_works = WorkPage.objects.filter(owner=self.owner).live().public().order_by('-first_published_at')
        return self.render(
            request,
            context_overrides={
                'all_works': all_works,
            },
            template = 'work/author_work.html',
        )


    @property
    def related_works(self):
        #owner = self.request.user()
        # get 4 pages with same services and exclude self page
        works = (
            WorkPage.objects.filter(owner=owner)
            .live()
            .distinct()
            .order_by("-id")
            .exclude(pk=self.pk)[:4]
        )
        return works


    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("screenshots", label="Screenshots"),
    ]


# Work index page
class WorkIndexPage(Page):
    template = "work/work_listing.html"

    max_count = 1

    parent_page_types = ["home.HomePage"]

    subpage_types = ["WorkPage"]

    intro = RichTextField(blank=True)

    hide_popular_tags = models.BooleanField(default=False)

    show_in_menus_default = True


    def get_context(self, request):
        context = super().get_context(request)
        all_works = WorkPage.objects.live().public().order_by('-first_published_at')
        

        paginator = Paginator(all_works, 20)

        page = request.GET.get('page')
        try:
            works = paginator.page(page)
        except PageNotAnInteger:
            works = paginator.page(1)
        except EmptyPage:
            works = paginator.page(paginator.num_pages)

        context['works'] = works
        return context

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("hide_popular_tags"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

