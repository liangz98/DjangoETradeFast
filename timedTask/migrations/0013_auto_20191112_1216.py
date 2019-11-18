# Generated by Django 2.2.1 on 2019-11-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0012_batches_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='receivable',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='currency_sum',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='discount_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='paid_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='post_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='service_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='trades',
            name='sum_sale',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
    ]
