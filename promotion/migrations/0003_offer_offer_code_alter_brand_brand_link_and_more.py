# Generated by Django 4.0.2 on 2022-02-15 14:25

from django.db import migrations, models
import promotion.models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0002_alter_offer_offer_expires_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_code',
            field=models.CharField(default="You don't need any code!", help_text='Leave this field empty for a deal.', max_length=20, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_link',
            field=models.CharField(max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(upload_to=promotion.models.rename_brand_logo, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_logo',
            field=models.ImageField(upload_to=promotion.models.rename_country_logos, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_details',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_title',
            field=models.CharField(max_length=20, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(choices=[('CODE', 'Code'), ('DEAL', 'Deal')], max_length=4, verbose_name='Type'),
        ),
    ]
