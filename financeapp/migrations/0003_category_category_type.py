# Generated by Django 5.1.4 on 2025-01-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0002_transaction_is_income_savingsgoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], default='expense', max_length=7),
        ),
    ]
