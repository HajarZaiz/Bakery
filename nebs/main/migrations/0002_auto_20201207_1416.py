# Generated by Django 3.1.3 on 2020-12-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Cake', 'Cake'), ('Bread', 'Bread'), ('Pastry', 'Pastry'), ('Cookies', 'Cookies'), ('Moroccan', 'Moroccan')], max_length=30),
        ),
    ]
