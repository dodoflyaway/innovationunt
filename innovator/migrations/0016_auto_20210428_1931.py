# Generated by Django 2.0.2 on 2021-04-28 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0015_auto_20210428_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invtokenacc',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovator.product'),
        ),
    ]