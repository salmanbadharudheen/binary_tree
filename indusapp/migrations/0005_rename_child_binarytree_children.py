# Generated by Django 4.2.2 on 2023-06-22 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indusapp', '0004_alter_binarytree_child_alter_binarytree_parent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='binarytree',
            old_name='child',
            new_name='children',
        ),
    ]
