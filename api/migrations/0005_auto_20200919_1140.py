# Generated by Django 3.1.1 on 2020-09-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200919_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='icon',
            field=models.CharField(blank=True, help_text='Enter icon class name for target site.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='icon',
            field=models.CharField(blank=True, help_text='Enter icon class name.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the category.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='link',
            name='to',
            field=models.CharField(help_text='Enter target location of link.', max_length=30),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(help_text='Enter link URL.'),
        ),
    ]
