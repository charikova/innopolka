# Generated by Django 2.0.1 on 2018-02-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0005_auto_20180204_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcopy',
            name='date',
            field=models.DateTimeField(default='2018-02-04 19:44'),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='returning_date',
            field=models.DateTimeField(default='2018-02-04 19:44'),
        ),
    ]
