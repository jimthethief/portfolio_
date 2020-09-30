# Generated by Django 3.0.8 on 2020-09-25 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200925_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.TextField(help_text="Enter a brief 'about me' intro.", max_length=1000),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter the section name.', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter a brief description of the category (optional).', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Which category does this language belong to? (optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat_languages', to='api.Category'),
        ),
        migrations.AlterField(
            model_name='language',
            name='logo_icon',
            field=models.CharField(blank=True, help_text='Enter icon class name (optional).', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(help_text='Must be unique - lower numbers appear more prominently.', unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the project.', max_length=1000),
        ),
    ]