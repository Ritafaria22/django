# Generated by Django 5.1.5 on 2025-02-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postapp/media/uploads/'),
        ),
    ]
