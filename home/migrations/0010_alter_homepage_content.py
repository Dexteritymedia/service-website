# Generated by Django 4.2.3 on 2023-08-27 20:53

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_service_image_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('slides', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(max_length=40, required=False)), ('body', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_page_text', wagtail.blocks.CharBlock(default='Find Out', max_length=40, required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first', required=False)), ('button_url_text', wagtail.blocks.CharBlock(default='Learn More', max_length=40, required=False))])))], label='Slides', max_num=3, min_num=3, template='home/blocks/slider_block.html')), ('feature', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Why Choose Us', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.blocks.TextBlock(required=False)), ('benefits', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('description', wagtail.blocks.RichTextBlock(max_length=40, required=False))])))], label='Features', template='home/blocks/feature_block.html')), ('project', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Our Projects/Portfolios', required=False)), ('projects', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))])))], label='Projects', template='home/blocks/project_block.html')), ('about_us', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(default='About Us', required=False)), ('description', wagtail.blocks.TextBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(page_type=['home.StaticPage'], required=False)), ('link_text', wagtail.blocks.CharBlock(default='Explore More')), ('benefits', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('description', wagtail.blocks.CharBlock(max_length=40, required=False)), ('completed_projects', wagtail.blocks.CharBlock(help_text='Enter a Number', max_length=40, required=False))])))], label='About us', template='home/blocks/about_block.html')), ('attribute', wagtail.blocks.StructBlock([('attributes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=40, required=False)), ('icon', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select an icon'), ('i2', 'Headphones'), ('i3', 'Check'), ('i4', 'Compass'), ('i5', 'Person'), ('i6', 'Arrow-right')], required=False))])))], label='Attributes', template='home/blocks/attribute_block.html')), ('team', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Team Members', label='Team Members', required=False)), ('teams', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('full_name', wagtail.blocks.CharBlock(default='Opabiyi Samson', help_text='Add your team member full name', max_length=40, required=True)), ('position', wagtail.blocks.CharBlock(default='Manager', help_text='Add your team member position', max_length=40, required=False)), ('facebook_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Facebook Username', max_length=40, required=False)), ('instagram_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Instagram Handle', max_length=40, required=False)), ('twitter_handle', wagtail.blocks.URLBlock(default='', help_text='Add your Twitter Handle', max_length=40, required=False))])))], label='Team', template='home/blocks/team_block.html'))], null=True, use_json_field=True),
        ),
    ]