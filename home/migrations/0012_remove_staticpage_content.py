# Generated by Django 4.2.3 on 2023-08-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_staticpage_content_alter_homepage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticpage',
            name='content',
        ),
    ]