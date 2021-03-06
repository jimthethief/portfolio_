# Generated by Django 3.1.1 on 2020-09-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200928_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='category',
        ),
        migrations.AddField(
            model_name='subject',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='Which category or categories is this subject related to? (optional)', null=True, related_name='cat_subjects', to='api.Category'),
        ),
    ]
