# Generated by Django 2.0.2 on 2021-04-28 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usern', '0002_auto_20210425_1339'),
        ('innovator', '0010_delete_sitetrans'),
    ]

    operations = [
        migrations.CreateModel(
            name='sitetrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transdate', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('key', models.IntegerField()),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usern.orduser')),
            ],
        ),
    ]
