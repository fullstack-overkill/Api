# Generated by Django 2.1.5 on 2019-07-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_userprofile_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='perfil',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
