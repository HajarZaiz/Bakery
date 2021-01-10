# Generated by Django 3.1.3 on 2020-12-19 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201207_1448'),
        ('shoppingcart', '0005_auto_20201213_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session',
            field=models.CharField(default='IDK', max_length=2000),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item')),
            ],
        ),
    ]
