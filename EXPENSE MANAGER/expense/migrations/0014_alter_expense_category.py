# Generated by Django 5.0.2 on 2024-03-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0013_remove_expense_transactiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
