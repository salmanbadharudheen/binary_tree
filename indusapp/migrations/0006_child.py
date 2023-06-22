# Generated by Django 4.2.2 on 2023-06-22 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indusapp', '0005_rename_child_binarytree_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childrens', models.CharField(max_length=255)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indusapp.binarytree')),
            ],
        ),
    ]