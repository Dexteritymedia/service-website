# Generated by Django 4.2.3 on 2023-09-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_alter_sitesettings_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='head_links',
            field=models.TextField(blank=True),
        ),
    ]
