# Generated by Django 5.1.5 on 2025-02-18 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='task',
        ),
    ]
