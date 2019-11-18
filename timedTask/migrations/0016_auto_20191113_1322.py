# Generated by Django 2.2.1 on 2019-11-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0015_salestockdetails_sale_stock_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='buyer_mobile',
            field=models.CharField(max_length=128, null=True, verbose_name='买家手机'),
        ),
        migrations.AddField(
            model_name='trades',
            name='express_code',
            field=models.CharField(max_length=256, null=True, verbose_name='快递单号'),
        ),
        migrations.AddField(
            model_name='trades',
            name='identity_name',
            field=models.CharField(max_length=256, null=True, verbose_name='身份证名称'),
        ),
        migrations.AddField(
            model_name='trades',
            name='identity_num',
            field=models.CharField(max_length=256, null=True, verbose_name='身份信息'),
        ),
        migrations.AddField(
            model_name='trades',
            name='jz_install_code',
            field=models.CharField(max_length=256, null=True, verbose_name='安装服务商编码-- 淘系家装类订单字段'),
        ),
        migrations.AddField(
            model_name='trades',
            name='jz_install_name',
            field=models.CharField(max_length=256, null=True, verbose_name='安装服务商名称-- 淘系家装类订单字段'),
        ),
        migrations.AddField(
            model_name='trades',
            name='jz_server_code',
            field=models.CharField(max_length=256, null=True, verbose_name='物流服务商编码-- 淘系家装类订单字段'),
        ),
        migrations.AddField(
            model_name='trades',
            name='jz_server_name',
            field=models.CharField(max_length=256, null=True, verbose_name='物流服务商名称-- 淘系家装类订单字段'),
        ),
        migrations.AddField(
            model_name='trades',
            name='logistic_code',
            field=models.CharField(max_length=256, null=True, verbose_name='万里牛ERP快递公司代码，用户自定义代码'),
        ),
        migrations.AddField(
            model_name='trades',
            name='print_remark',
            field=models.CharField(max_length=512, null=True, verbose_name='打印备注'),
        ),
        migrations.AddField(
            model_name='trades',
            name='print_time',
            field=models.DateTimeField(null=True, verbose_name='打单时间'),
        ),
        migrations.AddField(
            model_name='trades',
            name='remark',
            field=models.CharField(max_length=512, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='trades',
            name='sale_man',
            field=models.CharField(max_length=512, null=True, verbose_name='业务员'),
        ),
        migrations.AddField(
            model_name='trades',
            name='shop_id',
            field=models.CharField(max_length=128, null=True, verbose_name='shop_id'),
        ),
        migrations.AlterField(
            model_name='batches',
            name='inventory_id',
            field=models.UUIDField(null=True, verbose_name='库存本地UUID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='has_refund',
            field=models.IntegerField(default=0, verbose_name='是否退款'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='is_gift',
            field=models.BooleanField(default=False, verbose_name='明细是否赠品'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='oln_item_id',
            field=models.CharField(max_length=128, null=True, verbose_name='线上商品id'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='oln_item_name',
            field=models.CharField(max_length=256, null=True, verbose_name='线上商品名称'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='oln_sku_id',
            field=models.CharField(max_length=128, null=True, verbose_name='线上规格id'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='oln_status',
            field=models.IntegerField(default=0, verbose_name='上状态'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orders_id',
            field=models.CharField(max_length=128, null=True, verbose_name='明细id，单据级唯一'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='销售金额'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='单价(商品标价)'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='receivable',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='应收'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='size',
            field=models.IntegerField(default=0, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tp_oid',
            field=models.CharField(max_length=128, null=True, verbose_name='线上明细ID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tp_tid',
            field=models.CharField(max_length=128, null=True, verbose_name='线上单号'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='address',
            field=models.CharField(max_length=512, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='buyer',
            field=models.CharField(max_length=128, null=True, verbose_name='买家昵称'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='buyer_account',
            field=models.CharField(max_length=128, null=True, verbose_name='买家账号'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='buyer_msg',
            field=models.CharField(max_length=128, null=True, verbose_name='买家留言'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='city',
            field=models.CharField(max_length=128, null=True, verbose_name='市'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='country',
            field=models.CharField(max_length=128, null=True, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='create_time',
            field=models.DateTimeField(null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='currency_code',
            field=models.CharField(max_length=128, null=True, verbose_name='原始货币种类'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='currency_sum',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='原始货币金额'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='discount_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='优惠金额'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='district',
            field=models.CharField(max_length=128, null=True, verbose_name='区'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='完成时间：交易结束或交易成功的时间'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='flag',
            field=models.IntegerField(default=0, verbose_name='旗子颜色 0:无 1:红 2:黄 3:绿 4:蓝 5:粉'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='has_refund',
            field=models.BooleanField(default=False, verbose_name='是否有退款'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='is_exception_trade',
            field=models.BooleanField(default=False, verbose_name='是否异常订单'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='is_pay',
            field=models.BooleanField(default=False, verbose_name='是否已付款'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='is_small_trade',
            field=models.BooleanField(default=False, verbose_name='是否jit小单'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='mark',
            field=models.CharField(default=True, max_length=512, verbose_name='订单标记'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='modify_time',
            field=models.DateTimeField(null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='oln_order_list',
            field=models.CharField(default=False, max_length=512, verbose_name='明细线上单号集合'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='oln_status',
            field=models.IntegerField(default=0, verbose_name='线上状态 1:等待付款 2:等待发货,部分发货 3:已完成 4:已关闭 5:等待确认 6:已签收 0:未建交易'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='paid_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='实际支付金额'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='pay_no',
            field=models.CharField(max_length=128, null=True, verbose_name='外部支付单号'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='pay_time',
            field=models.DateTimeField(null=True, verbose_name='付款时间'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='pay_type',
            field=models.CharField(max_length=128, null=True, verbose_name='支付类型'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='phone',
            field=models.CharField(max_length=128, null=True, verbose_name='机号，手机号为空的时候返回电话'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='post_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='邮费'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='process_status',
            field=models.IntegerField(default=0, verbose_name='万里牛单据处理状态'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='province',
            field=models.CharField(max_length=128, null=True, verbose_name='省'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='receiver',
            field=models.CharField(max_length=256, null=True, verbose_name='收件人'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='seller_msg',
            field=models.CharField(max_length=512, null=True, verbose_name='卖家留言'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='send_time',
            field=models.DateTimeField(null=True, verbose_name='发货时间'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='service_fee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='服务费'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='shop_name',
            field=models.CharField(max_length=128, null=True, verbose_name='店铺名称(页面上显示)'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='shop_nick',
            field=models.CharField(max_length=128, null=True, verbose_name='店铺昵称(店铺唯一)'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='source_platform',
            field=models.CharField(max_length=128, null=True, verbose_name='订单来源平台'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态 1:处理中 2:发货 3:完成 4:关闭 5:其他'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='storage_code',
            field=models.CharField(max_length=128, null=True, verbose_name='仓库名称'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='storage_name',
            field=models.CharField(max_length=128, null=True, verbose_name='仓库编码'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='sum_sale',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='总金额,包含优惠'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='tp_tid',
            field=models.CharField(max_length=256, null=True, verbose_name='线上单号,如果是线下订单，则是万里牛的单号，合单情况下会将单号合并，使用|做分隔符'),
        ),
    ]
