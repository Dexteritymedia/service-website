# Generated by Django 4.2.3 on 2023-09-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('home', '0014_rename_intro_formpage_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='uploaded_image_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.collection'),
        ),
    ]