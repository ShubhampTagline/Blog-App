# Generated by Django 4.1.1 on 2022-09-20 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_alter_customuser_is_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogsdetails',
            old_name='blog_author',
            new_name='created_by',
        ),
    ]
