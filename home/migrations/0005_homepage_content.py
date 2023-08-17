# Generated by Django 4.2.3 on 2023-08-17 21:28

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('slides', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=40, required=False)), ('body', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=True)), ('color', wagtail.blocks.CharBlock(help_text='Enter a hexdecimal color for the background e.g #000000', max_length=40, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first', required=False))])))], label='Header', template='home/blocks/slider_block.html')), ('bustout', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.blocks.TextBlock(required=False)), ('benefits', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(max_length=40, required=False))])))], label='Features', template='home/blocks/feature_block.html')), ('project', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('projects', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=40, required=False)), ('description', wagtail.blocks.TextBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))])))], label='Project', template='home/blocks/project_block.html')), ('about_us', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.TextBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('benefits', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select an icon'), ('i2', 'Headset'), ('i3', 'Check'), ('i4', 'Compass'), ('i5', 'Person'), ('i6', 'Group')], required=False)), ('description', wagtail.blocks.CharBlock(max_length=40, required=False))])))], label='About us', template='home/blocks/about_block.html')), ('services', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('services', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=40, required=False)), ('description', wagtail.blocks.TextBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(page_type=['home.ServicePage'], required=False))])))], label='Service', template='home/blocks/service_block.html')), ('team', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Team Members', label='Team Members', required=False)), ('teams', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('full_name', wagtail.blocks.CharBlock(max_length=40, required=True)), ('position', wagtail.blocks.CharBlock(max_length=40, required=False)), ('facebook_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Facebook Username', max_length=40, required=False)), ('instagram_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Instagram Handle', max_length=40, required=False)), ('twitter_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Twitter Handle', max_length=40, required=False))])))], label='Team', template='home/blocks/team_block.html'))], null=True, use_json_field=True),
        ),
    ]