# Generated by Django 5.1.5 on 2025-02-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
