# Generated by Django 4.1.7 on 2023-05-19 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0011_remove_subcategory_cid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
