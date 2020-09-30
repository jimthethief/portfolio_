# Generated by Django 3.0.8 on 2020-09-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_category_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Section',
        ),
        migrations.AddField(
            model_name='category',
            name='section',
            field=models.ManyToManyField(blank=True, help_text='Which section(s) do you want to link this list to? (optional)', related_name='categories', to='api.Section'),
        ),
    ]