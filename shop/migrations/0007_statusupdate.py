# Generated by Django 3.2.6 on 2022-01-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_checkout_address_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
