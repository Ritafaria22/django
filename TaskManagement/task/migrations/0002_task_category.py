# Generated by Django 5.1.5 on 2025-02-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_catagory_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='category.catagory'),
        ),
    ]
