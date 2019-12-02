import uuid

from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# 订单
class Trades(models.Model):
    trade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_name = models.CharField("店铺名称(页面上显示)", max_length=128, null=True)
    shop_nick = models.CharField("店铺昵称(店铺唯一)", max_length=128, null=True)
    shop_id = models.CharField("shop_id", max_length=128, null=True)
    storage_name = models.CharField("仓库编码", max_length=128, null=True)
    storage_code = models.CharField("仓库名称", max_length=128, null=True)
    trade_no = models.CharField(max_length=128, null=True)
    oln_status = models.IntegerField("线上状态 1:等待付款 2:等待发货,部分发货 3:已完成 4:已关闭 5:等待确认 6:已签收 0:未建交易", default=0)
    buyer = models.CharField("买家昵称", max_length=128, null=True)
    buyer_account = models.CharField("买家账号", max_length=128, null=True)
    buyer_mobile = models.CharField("买家手机", max_length=128, null=True)
    buyer_msg = models.CharField("买家留言", max_length=128, null=True)
    receiver = models.CharField("收件人", max_length=256, null=True)
    phone = models.CharField("机号，手机号为空的时候返回电话", max_length=128, null=True)
    country = models.CharField("国家", max_length=128, null=True)
    province = models.CharField("省", max_length=128, null=True)
    city = models.CharField("市", max_length=128, null=True)
    district = models.CharField("区", max_length=128, null=True)
    address = models.CharField("地址", max_length=512, null=True)
    zip = models.CharField(max_length=64, default="")
    create_time = models.DateTimeField("创建时间", null=True)
    modify_time = models.DateTimeField("修改时间", null=True)
    send_time = models.DateTimeField("发货时间", null=True)
    pay_time = models.DateTimeField("付款时间", null=True)
    end_time = models.DateTimeField("完成时间：交易结束或交易成功的时间", null=True)
    status = models.IntegerField("状态 1:处理中 2:发货 3:完成 4:关闭 5:其他", default=0)
    is_pay = models.BooleanField("是否已付款", default=False)
    is_exception_trade = models.BooleanField("是否异常订单", default=False)
    tp_tid = models.CharField("线上单号,如果是线下订单，则是万里牛的单号，合单情况下会将单号合并，使用|做分隔符", max_length=256, null=True)
    source_platform = models.CharField("订单来源平台", max_length=128, null=True)
    sum_sale = models.DecimalField("总金额,包含优惠", default=0, max_digits=20, decimal_places=4)
    post_fee = models.DecimalField("邮费", default=0, max_digits=20, decimal_places=4)
    paid_fee = models.DecimalField("实际支付金额", default=0, max_digits=20, decimal_places=4)
    discount_fee = models.DecimalField("优惠金额", default=0, max_digits=20, decimal_places=4)
    service_fee = models.DecimalField("服务费", default=0, max_digits=20, decimal_places=4)
    has_refund = models.BooleanField("是否有退款", default=False)
    oln_order_list = models.CharField("明细线上单号集合", max_length=512, default=False)
    is_small_trade = models.BooleanField("是否jit小单", default=False)
    # 万里牛单据处理状态:
    # -3:分销商审核 -2:到账管理 -1:未付款 0:审核 1:打单配货 2:验货 3:称重 4:待发货 5：财审
    # 8:已发货 9:成功 10:关闭 11:异常结束 12:异常处理 13:外部系统配货中 14:预售 15:打包
    process_status = models.IntegerField("万里牛单据处理状态", default=0)
    trade_type = models.IntegerField(default=0)
    mark = models.CharField("订单标记", max_length=512, default=True)
    flag = models.IntegerField("旗子颜色 0:无 1:红 2:黄 3:绿 4:蓝 5:粉", default=0)
    pay_no = models.CharField("外部支付单号", max_length=128, null=True)
    pay_type = models.CharField("支付类型", max_length=128, null=True)
    express_code = models.CharField("快递单号", max_length=256, null=True)
    identity_name = models.CharField("身份证名称", max_length=256, null=True)
    identity_num = models.CharField("身份信息", max_length=256, null=True)
    jz_install_code = models.CharField("安装服务商编码-- 淘系家装类订单字段", max_length=256, null=True)
    jz_install_name = models.CharField("安装服务商名称-- 淘系家装类订单字段", max_length=256, null=True)
    jz_server_code = models.CharField("物流服务商编码-- 淘系家装类订单字段", max_length=256, null=True)
    jz_server_name = models.CharField("物流服务商名称-- 淘系家装类订单字段", max_length=256, null=True)
    logistic_code = models.CharField("万里牛ERP快递公司代码，用户自定义代码", max_length=256, null=True)
    currency_code = models.CharField("原始货币种类", max_length=128, null=True)
    currency_sum = models.DecimalField("原始货币金额", default=0, max_digits=20, decimal_places=4)
    print_remark = models.CharField("打印备注", max_length=512, null=True)
    print_time = models.DateTimeField("打单时间", null=True)
    remark = models.CharField("备注", max_length=512, null=True)
    sale_man = models.CharField("业务员", max_length=512, null=True)
    seller_msg = models.CharField("卖家留言", max_length=512, null=True)

    def __str__(self):
        return str(self.trade_id)


# 订单明细
class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trade_id = models.UUIDField()
    size = models.IntegerField("数量", default=0)
    price = models.DecimalField("单价(商品标价)", default=0, max_digits=20, decimal_places=4)
    receivable = models.DecimalField("应收", default=0, max_digits=20, decimal_places=4)
    payment = models.DecimalField("销售金额", default=0, max_digits=20, decimal_places=4)
    tp_tid = models.CharField("线上单号", max_length=128, null=True)
    oln_item_id = models.CharField("线上商品id", max_length=128, null=True)
    # 线上状态:1:等待付款 2:等待发货 ,部分发货 3:已完成 4:已关闭 5: 等待确认 6:已签收 0: 未建交易
    oln_status = models.IntegerField("上状态", default=0)
    oln_sku_id = models.CharField("线上规格id", max_length=128, null=True)
    # 状态:1:等待付款 2:等待发货 ,部分发货 3:已完成 4:已关闭 5: 等待确认 6:已签收 0: 未建交易
    status = models.IntegerField("状态", default=0)
    orders_id = models.CharField("明细id，单据级唯一", max_length=128, null=True)
    oln_item_name = models.CharField("线上商品名称", max_length=256, null=True)
    has_refund = models.IntegerField("是否退款", default=0)
    tp_oid = models.CharField("线上明细ID", max_length=128, null=True)
    is_gift = models.BooleanField("明细是否赠品", default=False)

    def __str__(self):
        return str(self.order_id)


# 商品
class Goods(models.Model):
    goods_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField("品牌名称", max_length=256, null=True)
    category_name = models.CharField("分类", max_length=128, null=True)
    expiration = models.IntegerField("保质期", default=0)
    goods_code = models.CharField("商品编码", max_length=128, null=True)
    goods_name = models.CharField("商品名称", max_length=512, null=True)
    manufacturer_name = models.CharField("生产商", max_length=256, null=True)
    pic = models.CharField("商品图片", max_length=512, null=True)
    purchase_num = models.FloatField("采购数量", default=0)
    purchase_type_name = models.CharField("采购类型", max_length=128, null=True)
    remark = models.CharField("备注", max_length=512, null=True)
    tag_price = models.DecimalField("吊牌价", default=0, max_digits=20, decimal_places=4)
    unit_name = models.CharField("单位", max_length=128, null=True)

    def __str__(self):
        return str(self.goods_id)


# 商品规格
class GoodsSpecs(models.Model):
    goods_spec_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goods_id = models.UUIDField(null=True)
    goods_code = models.CharField("商品编码", max_length=128, null=True)
    bar_code = models.CharField("条码", max_length=128, null=True)
    spec_code = models.CharField("规格编码", max_length=128, null=True)
    height = models.FloatField("高度", default=0)
    length = models.FloatField("长度", default=0)
    width = models.FloatField("宽度", default=0)
    weight = models.FloatField("重量", default=0)
    pic = models.CharField("图片", max_length=512, null=True)
    prime_price = models.DecimalField("参考进价", default=0, max_digits=20, decimal_places=4)
    sale_price = models.DecimalField("标准售价", default=0, max_digits=20, decimal_places=4)
    wholesale_price = models.DecimalField("批发价", default=0, max_digits=20, decimal_places=4)
    spec1 = models.CharField("规格1值", max_length=256, null=True)
    spec2 = models.CharField("规格2值", max_length=256, null=True)

    def __str__(self):
        return str(self.goods_spec_id)


# 规格
class Specs(models.Model):
    spec_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bar_code = models.CharField("条码", max_length=128, null=True)
    item_name = models.CharField("商品名称", max_length=512, null=True)
    spec_code = models.CharField("规格编码", max_length=128, null=True)
    color = models.CharField("颜色", max_length=128, null=True)
    price = models.DecimalField("标价", default=0, max_digits=20, decimal_places=4)
    article_number = models.CharField("货号", max_length=128, null=True)
    item_code = models.CharField("商品编码", max_length=128, null=True)
    category = models.CharField("品类", max_length=128, null=True)
    brand = models.CharField("品牌名称", max_length=256, null=True)
    other_prop = models.CharField("其他规格", max_length=256, null=True)
    unit = models.CharField("单位", max_length=128, null=True)
    prop1 = models.CharField("自定义规格", max_length=256, null=True)
    prop2 = models.CharField("自定义规格", max_length=256, null=True)
    prop3 = models.CharField("自定义规格", max_length=256, null=True)

    def __str__(self):
        return str(self.spec_id)


# 仓库
class Storage(models.Model):
    storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storage_code = models.CharField("仓库编码", max_length=256, null=True)
    storage_name = models.CharField("仓库名称", max_length=256, null=True)
    # 0禁用，1启用，2删除
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return str(self.storage_id)


# 库存
class Inventory(models.Model):
    inventory_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storage_id = models.UUIDField("仓库本地UUID", null=True)
    goods_code = models.CharField("商品编码", max_length=256, null=True)
    storage_code = models.CharField("仓库编码", max_length=256, null=True)
    lock_size = models.FloatField("锁定库存", default=0)
    quantity = models.FloatField("数量", default=0)
    sku_code = models.CharField("规格编码", max_length=256, null=True)
    underway = models.FloatField("在途库存", default=0)

    def __str__(self):
        return str(self.inventory_id)


# 批次
class Batches(models.Model):
    batch_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory_id = models.UUIDField("库存本地UUID", null=True)
    batch_no = models.CharField("批次编码", max_length=256, null=True)
    expired_date = models.DateTimeField("过期日期", null=True)
    num = models.FloatField("数量", default=0)
    produce_date = models.DateTimeField("成产日期", null=True)

    def __str__(self):
        return str(self.batch_id)


# 销售出库单
class SaleStock(models.Model):
    sale_stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bill_date = models.DateTimeField("单据日期", null=True)
    # 1-销售出库单 2-线下出库单
    bill_type = models.IntegerField("单据类型", default=0)
    country = models.CharField("国家", max_length=256, null=True)
    create_time = models.DateTimeField("创建时间", null=True)
    custom_code = models.CharField("客户编码", max_length=512, null=True)
    custom_name = models.CharField("客户名称", max_length=512, null=True)
    customer_nick = models.CharField("客户昵称", max_length=512, null=True)
    customer_nick_type = models.IntegerField("客户来源平台值", default=0)
    customer_nick_type_name = models.CharField("客户来源平台名称", max_length=512, null=True)
    discount_fee = models.DecimalField("优惠金额", default=0, max_digits=20, decimal_places=4)
    from_trade_no = models.CharField("万里牛中的原始交易编号,退货入库单中，关联的是出库单的单号", max_length=512, null=True)
    inv_no = models.CharField("单据编号", max_length=512, null=True)
    paid_fee = models.DecimalField("实际支付金额", default=0, max_digits=20, decimal_places=4)
    post_fee = models.DecimalField("邮费", default=0, max_digits=20, decimal_places=4)
    remark = models.CharField("备注", max_length=512, null=True)
    sale_man = models.CharField("业务员", max_length=512, null=True)
    service_fee = models.DecimalField("服务费", default=0, max_digits=20, decimal_places=4)
    shop_name = models.CharField("店铺名称", max_length=512, null=True)
    shop_nick = models.CharField("店铺昵称", max_length=512, null=True)
    shop_source = models.CharField("店铺来源", max_length=512, null=True)
    storage_code = models.CharField("仓库编码", max_length=512, null=True)
    sum_sale = models.DecimalField("总金额,包含优惠", default=0, max_digits=20, decimal_places=4)
    tp_tid = models.CharField("外部订单号", max_length=512, null=True)

    def __str__(self):
        return str(self.sale_stock_id)


# 销售出库单明细
class SaleStockDetails(models.Model):
    sale_stock_dDetail_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_stock_id = models.UUIDField("出库单UUID", null=True)
    goods_name = models.CharField("商品名称", max_length=512, null=True)
    discount_fee = models.DecimalField("优惠", default=0, max_digits=20, decimal_places=4)
    nums = models.FloatField("数量", default=0)
    sum_cost = models.DecimalField("成本", default=0, max_digits=20, decimal_places=4)
    sum_sale = models.DecimalField("总售价,包含优惠", default=0, max_digits=20, decimal_places=4)
    sku_name = models.CharField("sku名称", max_length=512, null=True)
    sku_no = models.CharField("sku编码", max_length=512, null=True)
    sku_prop1 = models.CharField("规格扩展属性", max_length=512, null=True)
    sku_prop2 = models.CharField("规格扩展属性", max_length=512, null=True)
    unit = models.CharField("单位", max_length=512, null=True)

    def __str__(self):
        return str(self.sale_stock_dDetail_id)


# 供应商
class Supplier(models.Model):
    supplier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier_code = models.CharField("供应商编码", max_length=256, null=True)
    supplier_name = models.CharField("供应商名称", max_length=256, null=True)
    # 1-启用，0-停用，-1-删除
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return str(self.supplier_id)
