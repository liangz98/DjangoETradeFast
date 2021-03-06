# Generated by Django 2.2.1 on 2019-11-12 15:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0013_auto_20191112_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleStock',
            fields=[
                ('sale_stock_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill_date', models.DateTimeField(null=True, verbose_name='单据日期')),
                ('bill_type', models.IntegerField(default=0, verbose_name='单据类型')),
                ('country', models.CharField(max_length=256, null=True, verbose_name='国家')),
                ('create_time', models.DateTimeField(null=True, verbose_name='创建时间')),
                ('custom_code', models.CharField(max_length=512, null=True, verbose_name='客户编码')),
                ('custom_name', models.CharField(max_length=512, null=True, verbose_name='客户名称')),
                ('customer_nick', models.CharField(max_length=512, null=True, verbose_name='客户昵称')),
                ('customer_nick_type', models.IntegerField(default=0, verbose_name='客户来源平台值')),
                ('customer_nick_type_name', models.CharField(max_length=512, null=True, verbose_name='客户来源平台名称')),
                ('discount_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='优惠金额')),
                ('from_trade_no', models.CharField(max_length=512, null=True, verbose_name='万里牛中的原始交易编号,退货入库单中，关联的是出库单的单号')),
                ('inv_no', models.CharField(max_length=512, null=True, verbose_name='单据编号')),
                ('paid_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='实际支付金额')),
                ('post_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='邮费')),
                ('remark', models.CharField(max_length=512, null=True, verbose_name='备注')),
                ('sale_man', models.CharField(max_length=512, null=True, verbose_name='业务员')),
                ('service_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='服务费')),
                ('shop_name', models.CharField(max_length=512, null=True, verbose_name='店铺名称')),
                ('shop_nick', models.CharField(max_length=512, null=True, verbose_name='店铺昵称')),
                ('shop_source', models.CharField(max_length=512, null=True, verbose_name='店铺来源')),
                ('storage_code', models.CharField(max_length=512, null=True, verbose_name='仓库编码')),
                ('sum_sale', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='总金额,包含优惠')),
                ('tp_tid', models.CharField(max_length=512, null=True, verbose_name='外部订单号')),
            ],
        ),
        migrations.CreateModel(
            name='SaleStockDetails',
            fields=[
                ('sale_stock_dDetail_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=512, null=True, verbose_name='商品名称')),
                ('discount_fee', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='优惠')),
                ('nums', models.FloatField(default=0, verbose_name='数量')),
                ('sum_cost', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='成本')),
                ('sum_sale', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='总售价,包含优惠')),
                ('sku_name', models.CharField(max_length=512, null=True, verbose_name='sku名称')),
                ('sku_no', models.CharField(max_length=512, null=True, verbose_name='sku编码')),
                ('sku_prop1', models.CharField(max_length=512, null=True, verbose_name='规格扩展属性')),
                ('sku_prop2', models.CharField(max_length=512, null=True, verbose_name='规格扩展属性')),
                ('unit', models.CharField(max_length=512, null=True, verbose_name='单位')),
            ],
        ),
        migrations.AlterField(
            model_name='goods',
            name='tag_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='吊牌价'),
        ),
        migrations.AlterField(
            model_name='goodsspecs',
            name='prime_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='参考进价'),
        ),
        migrations.AlterField(
            model_name='goodsspecs',
            name='sale_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='标准售价'),
        ),
        migrations.AlterField(
            model_name='goodsspecs',
            name='wholesale_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='批发价'),
        ),
        migrations.AlterField(
            model_name='specs',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='标价'),
        ),
    ]
