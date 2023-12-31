# Generated by Django 4.2.3 on 2023-08-17 21:06

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('service_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('images', wagtail.fields.StreamField([('photos', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))], blank=True, null=True, use_json_field=True)),
            ],
            options={
                'verbose_name': 'Service detail',
                'verbose_name_plural': 'Service details',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('call_to_action', wagtail.fields.StreamField([('key_points_summary', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock())]), help_text='Please add a minumum of 4 and a maximum of 6 key points.', icon='list-ul', max_num=6, min_num=4, template='blocks/key_points_summary.html')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('name', wagtail.blocks.CharBlock()), ('role', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='openquote', template='blocks/testimonial_block.html')), ('clients', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='site', label='Clients logo', template='blocks/client-logo-block.html')), ('embed_plus_cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(label='External Link', required=False)), ('button_text', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(label='Youtube Embed', required=False))], icon='code', label='Embed + CTA', template='blocks/embed_plus_cta_block.html')), ('cta', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Words in  &lt;span&gt; tag will display in a contrasting colour.')), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))]))], icon='plus-inverse', template='blocks/cta.html'))], blank=True, null=True, use_json_field=True)),
                ('body', wagtail.fields.StreamField([('h2', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading2_block.html')), ('h3', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading3_block.html')), ('h4', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading4_block.html')), ('intro', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/intro_block.html')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.blocks.CharBlock()), ('attribution', wagtail.blocks.CharBlock(required=False))], label='Aligned image', template='blocks/aligned_image_block.html')), ('wide_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], label='Wide image', template='blocks/wide_image_block.html')), ('bustout', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.RichTextBlock())], template='blocks/bustout_block.html')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('attribution', wagtail.blocks.CharBlock())], template='blocks/pullquote_block.html')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML', template='blocks/raw_html_block.html')), ('mailchimp_form', wagtail.blocks.RawHTMLBlock(icon='code', label='Mailchimp embedded form', template='blocks/mailchimp_form_block.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Media', icon='code', template='blocks/embed_block.html'))], null=True, use_json_field=True)),
            ],
            options={
                'verbose_name': 'Other Page',
                'verbose_name_plural': 'Other Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
