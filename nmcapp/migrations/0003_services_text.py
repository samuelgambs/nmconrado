# Generated by Django 2.0.1 on 2018-01-05 05:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nmcapp', '0002_auto_20180105_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='text',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
