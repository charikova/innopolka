# Generated by Django 2.0.1 on 2018-02-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0012_auto_20180206_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcopy',
            name='date',
            field=models.DateTimeField(default='2018-02-06 21:42'),
        ),
        migrations.AlterField(
            model_name='documentcopy',
            name='returning_date',
            field=models.DateTimeField(default='2018-02-06 21:42'),
        ),
    ]
