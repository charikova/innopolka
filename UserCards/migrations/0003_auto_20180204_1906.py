# Generated by Django 2.0.1 on 2018-02-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserCards', '0002_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.CharField(default='https://lh3.googleusercontent.com/zqfUbCXdb1oGmsNEzNxTjQU5ZlS3x46nQoB83sFbRSlMnpDTZgdVCe_LvCx-rl7sOA=w300', max_length=1000),
        ),
    ]
