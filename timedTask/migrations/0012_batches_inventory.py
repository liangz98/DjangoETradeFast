# Generated by Django 2.2.1 on 2019-11-11 18:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0011_auto_20191111_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('batch_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inventory_id', models.UUIDField(null=True, verbose_name='仓库本地UUID')),
                ('batch_no', models.CharField(max_length=256, null=True, verbose_name='批次编码')),
                ('expired_date', models.DateTimeField(null=True, verbose_name='过期日期')),
                ('num', models.FloatField(default=0, verbose_name='数量')),
                ('produce_date', models.DateTimeField(null=True, verbose_name='成产日期')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('storage_id', models.UUIDField(null=True, verbose_name='仓库本地UUID')),
                ('goods_code', models.CharField(max_length=256, null=True, verbose_name='商品编码')),
                ('storage_code', models.CharField(max_length=256, null=True, verbose_name='仓库编码')),
                ('lock_size', models.FloatField(default=0, verbose_name='锁定库存')),
                ('quantity', models.FloatField(default=0, verbose_name='数量')),
                ('sku_code', models.CharField(max_length=256, null=True, verbose_name='规格编码')),
                ('underway', models.FloatField(default=0, verbose_name='在途库存')),
            ],
        ),
    ]
