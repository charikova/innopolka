# Generated by Django 2.0.1 on 2018-01-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0010_auto_20180120_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(default='document', max_length=100),
        ),
    ]
