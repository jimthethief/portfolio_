# Generated by Django 3.0.8 on 2020-09-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200919_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='category',
            field=models.CharField(blank=True, choices=[('FRO', 'Frontend'), ('BAC', 'Backend'), ('FRA', 'Framework/Library'), ('MAR', 'Markup'), ('OTH', 'Other')], help_text='Choose the primary category for the language', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(help_text='Lower numbers appear more prominently', unique=True),
        ),
    ]