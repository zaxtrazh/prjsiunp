# Generated by Django 2.2 on 2020-02-20 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0003_userprofiles_alamat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofiles',
            old_name='user',
            new_name='namaUser',
        ),
    ]
