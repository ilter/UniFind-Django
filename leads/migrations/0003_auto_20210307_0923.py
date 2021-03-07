# Generated by Django 3.1.7 on 2021-03-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210307_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='last_name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='first_name',
            new_name='university_name',
        ),
        migrations.RemoveField(
            model_name='university',
            name='special_files',
        ),
        migrations.AddField(
            model_name='university',
            name='admission_status',
            field=models.BooleanField(default=False),
        ),
    ]
