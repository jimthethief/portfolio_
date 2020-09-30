# Generated by Django 3.1.1 on 2020-09-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200919_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlanguage',
            name='percent_used',
            field=models.IntegerField(blank=True, help_text='Enter a number between 1 and 100 to signify language usage (optional).', null=True),
        ),
    ]
