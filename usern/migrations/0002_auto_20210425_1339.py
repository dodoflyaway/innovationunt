# Generated by Django 2.0.2 on 2021-04-25 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usern', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orduser',
            old_name='naddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nfirstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nlastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='npassword1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='npassword2',
            new_name='password2',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nphone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nuser_type',
            new_name='user_type',
        ),
        migrations.RenameField(
            model_name='orduser',
            old_name='nusername',
            new_name='username',
        ),
    ]
