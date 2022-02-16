# Generated by Django 4.0.2 on 2022-02-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0006_alter_brand_brand_logo_alter_country_country_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_slug',
            field=models.SlugField(default='country-slug', help_text='Re-enter the brand name here again.', unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='country_slug',
            field=models.SlugField(default='brand-slug', help_text='Re-enter the country name here again.', unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]