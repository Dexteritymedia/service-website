# Generated by Django 4.2.3 on 2023-09-05 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_alter_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]
