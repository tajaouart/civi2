# Generated by Django 3.0.6 on 2020-05-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cvjson'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='CV',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='PersonalInformation',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Studie',
        ),
    ]
