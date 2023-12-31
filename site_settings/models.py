from django.db import models

# Create your models here.
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable

from modelcluster.fields import ParentalKey

from home.blocks import HeaderLinkBlock

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    instagram = models.URLField(max_length=100, default='@genius', null=True, blank=True, help_text='Enter your instagram username')
    facebook = models.URLField(max_length=100, default='Genius multi-concept', null=True, blank=True, help_text='Enter your facebook ID or name')
    twitter = models.URLField(max_length=100, default='@genius', null=True, blank=True, help_text='Enter your twitter username')
    pinterest = models.URLField(max_length=100, default='@genius', null=True, blank=True, help_text='pinterest username')
    linkedin = models.URLField(max_length=100, default='@genius', null=True, blank=True, help_text='Your linkedin username')
    whatsapp = models.CharField(max_length=100, default='Enter your WhatsApp number', null=True, blank=True, help_text='Your whatsapp number')
    
    panels = [
        MultiFieldPanel([
            
            FieldPanel('instagram'),
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('pinterest'),
            FieldPanel('linkedin'),
            FieldPanel('whatsapp'),
        ], heading="Social Media")
        ]

    class Meta:
        verbose_name = 'Social Media Channel'

"""
class HeaderLinks(Orderable):
    page = ParentalKey("site_settings.SiteSettings", related_name="header_links")
    link = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel("link"),
    ]
"""

@register_setting
class SiteSettings(BaseSiteSetting):
    site_name = models.CharField(max_length=100, null=True, blank=True, help_text='Your website name')
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        help_text='Your website logo',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    show_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show logo in menu bar', verbose_name='Menu Logo',)
    show_title_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show Title in menu bar', verbose_name='Menu Title',)
    api_key = models.CharField(max_length=100, null=True, blank=True, verbose_name='Google Maps API Key', help_text='The API Key used for Google Maps')
    map_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Map Title', help_text='Map Title for Screen readers, ex: Map to Goodale Park')
    place_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='Google Place ID', help_text='Requires API Key to use place ID')
    map_zoom_level = models.IntegerField(null=True, verbose_name='Map zoom level', blank=True, help_text='Requires API Key to use zoom. 1: World, 5: Landmass/Continent, 10: City, 15: Streets, 20: Buildings')
    search = models.CharField(blank=True, verbose_name='Search', help_text='Address or search term used to find your location on the map', max_length=250)
    shop_address = models.CharField(blank=True, verbose_name='Shop Address', help_text='Address or search term used to find your location', default="Shop A7/A8 Ido Shopping Complex Apete Ibadan, Oyo State, Nigeria", max_length=250)
    time_and_date = RichTextField(verbose_name='Time and Day', blank=True,)
    phone_no = models.CharField(blank=True, verbose_name='Phone number', help_text='Your office phone number', max_length=250)
    email = models.EmailField(blank=True, verbose_name='Email', help_text='Enter your email address', max_length=250)
    header_links = models.TextField(blank=True, verbose_name='Links', help_text="Use this to add links, scripts such as google analytics to the head section of the website")

    
    panels = [
        MultiFieldPanel([
            FieldPanel('site_name'),
            FieldPanel('show_title_in_menu_bar'),
            ]),
        
        MultiFieldPanel([
            FieldPanel('site_logo'),
            FieldPanel('show_in_menu_bar'),
            FieldPanel('caption'),
        ], heading="Website Image"),

        MultiFieldPanel([
            FieldPanel('phone_no'),
            FieldPanel('shop_address'),
            FieldPanel('email'),
            FieldPanel('time_and_date'),
        ], heading="Website Details and Address"),

        MultiFieldPanel([
            FieldPanel('api_key'),
            FieldPanel('search'),
            FieldPanel('map_title'),
            FieldPanel('place_id'),
            FieldPanel('map_zoom_level'),
            ], heading='Settings for Google Map'),

        MultiFieldPanel([
            FieldPanel('header_links'),
            ], heading='Add links'),

        #InlinePanel("header_links", label="Header Links"),

        ]

    class Meta:
        verbose_name = 'Site Setting'
