# Generated by Django 4.1.1 on 2022-09-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0023_rename_blog_id_comment_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsdetails',
            name='blog_content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='blogsdetails',
            name='blog_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
    ]
