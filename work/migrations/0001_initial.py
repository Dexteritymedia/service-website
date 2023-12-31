# Generated by Django 4.2.3 on 2023-08-27 21:28

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import modelcluster.fields
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('partners', '0002_author'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('sort_order', models.IntegerField()),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('hide_popular_tags', models.BooleanField(default=False)),
                ('call_to_action', wagtail.fields.StreamField([('key_points_summary', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock())]), help_text='Please add a minumum of 4 and a maximum of 6 key points.', icon='list-ul', max_num=6, min_num=4, template='blocks/key_points_summary.html')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('name', wagtail.blocks.CharBlock()), ('role', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='openquote', template='blocks/testimonial_block.html')), ('clients', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='site', label='Clients logo', template='blocks/client-logo-block.html')), ('embed_plus_cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(label='External Link', required=False)), ('button_text', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(label='Youtube Embed', required=False))], icon='code', label='Embed + CTA', template='blocks/embed_plus_cta_block.html')), ('cta', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Words in  &lt;span&gt; tag will display in a contrasting colour.')), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))]))], icon='plus-inverse', template='blocks/cta.html'))], blank=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WorkPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(null=True, verbose_name='Post date')),
                ('body', wagtail.fields.StreamField([('h2', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading2_block.html')), ('h3', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading3_block.html')), ('h4', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='blocks/heading4_block.html')), ('intro', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/intro_block.html')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.blocks.CharBlock()), ('attribution', wagtail.blocks.CharBlock(required=False))], label='Aligned image', template='blocks/aligned_image_block.html')), ('wide_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], label='Wide image', template='blocks/wide_image_block.html')), ('bustout', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.RichTextBlock())], template='blocks/bustout_block.html')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('attribution', wagtail.blocks.CharBlock())], template='blocks/pullquote_block.html')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML', template='blocks/raw_html_block.html')), ('mailchimp_form', wagtail.blocks.RawHTMLBlock(icon='code', label='Mailchimp embedded form', template='blocks/mailchimp_form_block.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Media', icon='code', template='blocks/embed_block.html'))], use_json_field=True)),
                ('body_word_count', models.PositiveIntegerField(editable=False, null=True)),
                ('visit_the_site', models.URLField(blank=True)),
                ('listing_summary', models.CharField(blank=True, max_length=255)),
                ('client', models.TextField(blank=True)),
                ('call_to_action', wagtail.fields.StreamField([('key_points_summary', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock())]), help_text='Please add a minumum of 4 and a maximum of 6 key points.', icon='list-ul', max_num=6, min_num=4, template='blocks/key_points_summary.html')), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('name', wagtail.blocks.CharBlock()), ('role', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='openquote', template='blocks/testimonial_block.html')), ('clients', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))], required=False))]), icon='site', label='Clients logo', template='blocks/client-logo-block.html')), ('embed_plus_cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('intro', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(label='External Link', required=False)), ('button_text', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(label='Youtube Embed', required=False))], icon='code', label='Embed + CTA', template='blocks/embed_plus_cta_block.html')), ('cta', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Words in  &lt;span&gt; tag will display in a contrasting colour.')), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))]))], icon='plus-inverse', template='blocks/cta.html'))], blank=True, use_json_field=True)),
                ('feed_image', models.ForeignKey(blank=True, help_text='Image used on listings and social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('homepage_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('related_services', modelcluster.fields.ParentalManyToManyField(related_name='case_studies', to='work.service')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WorkPageTagSelect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='work.workpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_page_tag_select', to='work.tag')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkPageScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='work.workpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkPageAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='partners.author')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='work.workpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
