# Generated by Django 2.0.7 on 2018-10-02 20:28

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contactsmanagement', '0003_contactmanagements_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmanagements',
            name='address',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='city',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='country',
            field=django_countries.fields.CountryField(default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='note',
            field=models.TextField(default=None, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='postcode',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='state',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmanagements',
            name='street',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
