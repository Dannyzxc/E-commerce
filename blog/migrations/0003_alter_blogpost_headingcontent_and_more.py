# Generated by Django 4.0.1 on 2022-01-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_content_blogpost_headingcontent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='headingContent',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='subHeadingContent',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='titleContent',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
