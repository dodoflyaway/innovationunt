# Generated by Django 2.0.2 on 2021-04-29 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0016_auto_20210428_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invtokenacc',
            name='inuser',
        ),
        migrations.RemoveField(
            model_name='invtokenacc',
            name='key',
        ),
        migrations.DeleteModel(
            name='invtokenacc',
        ),
    ]
