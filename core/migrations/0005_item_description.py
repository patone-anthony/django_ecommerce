# Generated by Django 2.2.8 on 2020-01-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='this is a test description lka;sjdflk'),
            preserve_default=False,
        ),
    ]
