# Generated by Django 4.2.2 on 2023-06-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indusapp', '0003_binarytree_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binarytree',
            name='child',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='binarytree',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indusapp.binarytree'),
        ),
    ]
