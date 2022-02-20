# Generated by Django 4.0.2 on 2022-02-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0010_brand_brand_slug_country_country_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_slug',
            field=models.SlugField(editable=False),
        ),
    ]
