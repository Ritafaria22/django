# Generated by Django 5.1.5 on 2025-02-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathername',
            field=models.TextField(default='rahim'),
        ),
    ]
