# Generated by Django 2.0.2 on 2021-04-26 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('innovator', '0004_remove_subcribe_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='subz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zsub_username', models.CharField(max_length=200)),
                ('zordinary_username', models.CharField(max_length=200)),
                ('zlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovator.invuser')),
            ],
        ),
        migrations.DeleteModel(
            name='subcribe',
        ),
    ]
