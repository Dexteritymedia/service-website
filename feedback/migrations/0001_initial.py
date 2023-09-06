# Generated by Django 4.2.3 on 2023-09-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your first name and surname', max_length=500)),
                ('message', models.TextField(help_text='Write your message ')),
                ('ratings', models.CharField(help_text='Please rate our services between 1 to 5', max_length=50)),
                ('picture', models.ImageField(blank=True, help_text='Please upload a picture you would love to appear on the review', upload_to='')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
