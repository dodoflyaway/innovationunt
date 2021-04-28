# Generated by Django 2.0.2 on 2021-04-25 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('innovator_username', models.CharField(max_length=200)),
                ('ordinary_username', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovator.invuser')),
            ],
        ),
    ]