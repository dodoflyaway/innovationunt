# Generated by Django 2.0.2 on 2021-04-29 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0018_invtokenacc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invtokenacc',
            name='inuser',
        ),
        migrations.RemoveField(
            model_name='invtokenacc',
            name='keyh',
        ),
        migrations.RemoveField(
            model_name='sitetrans',
            name='holder',
        ),
        migrations.DeleteModel(
            name='invtokenacc',
        ),
        migrations.DeleteModel(
            name='sitetrans',
        ),
    ]