# Generated by Django 3.2.16 on 2022-10-17 23:17

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_file',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.patients_image_file_path),
        ),
    ]