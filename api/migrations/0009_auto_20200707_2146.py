# Generated by Django 3.0.3 on 2020-07-07 21:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/melodic/dev/python/civi2/'), upload_to='static'),
        ),
    ]
