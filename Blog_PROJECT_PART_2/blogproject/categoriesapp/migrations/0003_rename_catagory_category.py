# Generated by Django 5.1.5 on 2025-02-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoriesapp', '0002_catagory_slug'),
        ('postapp', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]
