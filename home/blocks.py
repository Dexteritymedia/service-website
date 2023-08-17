from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.functional import cached_property

from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    FieldBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    URLBlock,
    ChoiceBlock,
    TextBlock,
    ChooserBlock,
)
from wagtail.blocks.struct_block import StructBlockValidationError
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class LinkStructValue(StructValue):
    @cached_property
    def url(self):
        if page := self.get("page"):
            return page.get_url()
        elif link_url := self.get("link_url"):
            return link_url

    @cached_property
    def text(self):
        if link_text := self.get("link_text"):
            return link_text
        elif page := self.get("page"):
            return page.title

#New Blocks
class SliderBlock(StructBlock):

    slides = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', CharBlock(required=False, max_length=40)),
                ('body', RichTextBlock(required=True, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link'],)),
                ('color', CharBlock(required=False, max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")),
                ('button_page', PageChooserBlock(required=False)),
                ('button_url', URLBlock(required=False, help_text='If the button page above is selected, that will be used first')),
            ]
        )
    )


    class Meta:
        icon = "list-ul"
        max_num = 1


class AboutUsBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    title = CharBlock(required=False)
    description = TextBlock(required=False)
    link = PageChooserBlock(required=False)
    benefits = ListBlock(
        StructBlock(
            [
                ('icon', ChoiceBlock(choices=[
                    ('', 'Select an icon'),
                    ('i2', 'Headset'),
                    ('i3', 'Check'),
                    ('i4', 'Compass'),
                    ('i5', 'Person'),
                    ('i6', 'Group')
                ], blank=True, required=False)
                ),
                ('description', CharBlock(required=False, max_length=40)),
            ]
        )
    )
    
    class Meta:
        icon = 'form'
        


class ServiceBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    heading = CharBlock(required=False)
    
    services = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', CharBlock(required=False, max_length=40)),
                ('description', TextBlock(required=False)),
                ('link', PageChooserBlock(required=False, target_model=['home.ServicePage'])),
            ]
        )
    )
    
    class Meta:
        icon = 'site'
        template = "home/blocks/service_block.html"
        label = "Service"
       

class TeamBlock(StructBlock):

    heading = CharBlock(default='Team Members', label='Team Members', required=False)
    
    teams = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('full_name', CharBlock(required=True, max_length=40)),
                ('position', CharBlock(required=False, max_length=40)),
                ('facebook_handle', URLBlock(required=False, default='', help_text="Add your Facebook Username", max_length=40)),
                ('instagram_handle', URLBlock(required=False, default='', help_text="Add your Instagram Handle", max_length=40)),
                ('twitter_handle', URLBlock(required=False, default='', help_text="Add your Twitter Handle", max_length=40)),
            ]
        )
    )
    
    class Meta:
        icon = 'group'
      

class ProjectBlock(StructBlock):
    heading = CharBlock(required=False)
    
    projects = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', CharBlock(required=False, max_length=40)),
                ('description', TextBlock(required=False)),
                ('link', PageChooserBlock(required=False)),
            ]
        )
    )
    
    class Meta:
        icon = 'grip'


class FeatureBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    heading = CharBlock(required=False)
    image = ImageChooserBlock(required=True)
    body = TextBlock(required=False)
    benefits = ListBlock(
        StructBlock(
            [
                ('icon', ImageChooserBlock(required=False)),
                ('description', RichTextBlock(required=False, max_length=40)),
            ]
        )
    )
    
    class Meta:
        icon = 'pick'


class HeaderLinkBlock(StructBlock):
    code = TextBlock(required=False)

    class Meta:
        label = "Link"
        icon = "link"


class HomePageBlock(StreamBlock):
    heading = SliderBlock(
        template = "home/blocks/slider_block.html",
        label = "Header",
        min_num=3,
        max_num=3,
    )
    feature = FeatureBlock(
        template = "home/blocks/feature_block.html",
        label = "Features"
    )
    project =  ProjectBlock(
        template = "home/blocks/project_block.html",
        label = "Project"
    )
    about_us  = AboutUsBlock(
        template = "home/blocks/about_block.html",
        label = "About us"
    )
    services = ServiceBlock(
        template = "home/blocks/service_block.html",
        label = "Service"
    )
    team = TeamBlock(
        template = "home/blocks/team_block.html",
        label = "Team"
    )
    


#Torchbox blocks
class InternalLinkBlock(StructBlock):
    page = PageChooserBlock()
    link_text = CharBlock(required=False)

    class Meta:
        label = "Internal link"
        icon = "link"
        value_class = LinkStructValue


class ExternalLinkBlock(StructBlock):
    link_url = URLBlock(label="URL")
    link_text = CharBlock()

    class Meta:
        label = "External link"
        icon = "link"
        value_class = LinkStructValue


class LinkBlock(StreamBlock):
    internal_link = InternalLinkBlock()
    external_link = ExternalLinkBlock()

    class Meta:
        label = "Link"
        icon = "link"
        max_num = 1


class KeyPoint(StructBlock):
    title = CharBlock()
    intro = CharBlock()
    link = PageChooserBlock()

    class Meta:
        icon = "form"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(
        choices=(
            ("left", "Wrap left"),
            ("right", "Wrap right"),
            ("half", "Half width"),
            ("full", "Full width"),
        )
    )


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()
    caption = CharBlock()
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"
        label = "Image"


class ImageWithLinkBlock(StructBlock):
    image = ImageChooserBlock()
    link = LinkBlock(required=False)

    class Meta:
        icon = "site"


class PhotoGridBlock(StructBlock):
    images = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "grip"
        min_num = 1
        max_num = 1


class PullQuoteBlock(StructBlock):
    quote = CharBlock(form_classname="quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class PullQuoteImageBlock(StructBlock):
    quote = CharBlock()
    attribution = CharBlock()
    image = ImageChooserBlock(required=False)


class TestimonialBlock(StructBlock):
    quote = CharBlock(form_classname="quote title")
    name = CharBlock()
    role = CharBlock()
    link = LinkBlock(required=False)

    class Meta:
        icon = "openquote"


class BustoutBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()

    class Meta:
        icon = "pick"


class WideImage(StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = "image"
        min_num = 1
        max_num = 1
        block_counts = {
            'image': {'min_num': 1, 'max_num': 1},
        }


class StatsBlock(StructBlock):
    pass

    class Meta:
        icon = "order"


class EmbedPlusCTABlock(StructBlock):
    title = CharBlock()
    intro = CharBlock()
    link = PageChooserBlock(required=False)
    external_link = URLBlock(label="External Link", required=False)
    button_text = CharBlock()
    image = ImageChooserBlock(required=False)
    embed = EmbedBlock(required=False, label="Youtube Embed")

    def clean(self, value):
        struct_value = super().clean(value)

        errors = {}
        image = value.get("image")
        embed = value.get("embed")

        if image and embed:
            error = ErrorList(
                [
                    ValidationError(
                        "Either an image or a Youtube embed may be specified, but not both."
                    )
                ]
            )
            errors["image"] = errors["embed"] = error

        if errors:
            raise StructBlockValidationError(errors)
        return struct_value


class CTABlock(StructBlock):
    text = CharBlock(
        help_text="Words in  &lt;span&gt; tag will display in a contrasting colour."
    )
    link = LinkBlock()


class StoryBlock(StreamBlock):
    h2 = CharBlock(
        form_classname="title",
        icon="title",
        template="blocks/heading2_block.html",
    )
    h3 = CharBlock(
        form_classname="title",
        icon="title",
        template="blocks/heading3_block.html",
    )
    h4 = CharBlock(
        form_classname="title",
        icon="title",
        template="blocks/heading4_block.html",
    )
    intro = RichTextBlock(
        icon="pilcrow",
        template="blocks/intro_block.html",
    )
    paragraph = RichTextBlock(
        icon="pilcrow",
        template="blocks/paragraph_block.html",
    )
    aligned_image = ImageBlock(
        label="Aligned image",
        template="blocks/aligned_image_block.html",
    )
    wide_image = WideImage(
        label="Wide image",
        template="blocks/wide_image_block.html",
    )
    bustout = BustoutBlock(
        template="blocks/bustout_block.html"
    )
    pullquote = PullQuoteBlock(
        template="blocks/pullquote_block.html"
    )
    raw_html = RawHTMLBlock(
        label="Raw HTML",
        icon="code",
        template="blocks/raw_html_block.html",
    )
    mailchimp_form = RawHTMLBlock(
        label="Mailchimp embedded form",
        icon="code",
        template="blocks/mailchimp_form_block.html",
    )
    embed = EmbedBlock(
        icon="code",
        template="blocks/embed_block.html",
        group="Media",
    )

    class Meta:
        template = "blocks/stream_block.html"


class PageSectionStoryBlock(StreamBlock):
    key_points_summary = ListBlock(
        KeyPoint(),
        icon="list-ul",
        min_num=4,
        max_num=6,
        template="blocks/key_points_summary.html",
        help_text="Please add a minumum of 4 and a maximum of 6 key points.",
    )
    testimonials = ListBlock(
        TestimonialBlock(),
        icon="openquote",
        template="blocks/testimonial_block.html",
    )
    clients = ListBlock(
        ImageWithLinkBlock(),
        icon="site",
        template="blocks/client-logo-block.html",
        label="Clients logo",
    )
    embed_plus_cta = EmbedPlusCTABlock(
        label="Embed + CTA",
        icon="code",
        template="blocks/embed_plus_cta_block.html",
    )
    cta = CTABlock(
        icon="plus-inverse",
        template="blocks/cta.html",
    )

    class Meta:
        template = "blocks/stream_block.html"
