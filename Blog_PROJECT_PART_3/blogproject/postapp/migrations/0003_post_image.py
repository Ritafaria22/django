# Generated by Django 5.1.5 on 2025-02-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
