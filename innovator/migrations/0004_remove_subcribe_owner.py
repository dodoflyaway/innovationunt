# Generated by Django 2.0.2 on 2021-04-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0003_subcribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcribe',
            name='owner',
        ),
    ]
