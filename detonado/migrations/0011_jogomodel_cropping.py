# Generated by Django 3.0.8 on 2020-08-05 23:16

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('detonado', '0010_auto_20200804_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogomodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('thumbnail', '900x900', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
