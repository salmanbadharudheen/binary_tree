# Generated by Django 4.2.2 on 2023-06-22 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indusapp', '0007_rename_childrens_child_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binarytree',
            name='children',
        ),
    ]
