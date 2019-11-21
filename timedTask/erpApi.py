import datetime
import hashlib
import time
import requests
import logging

from django.utils import timezone

from timedTask.models import Trades, Orders, Specs, Storage, Supplier, Goods, GoodsSpecs, Inventory, Batches, SaleStock, SaleStockDetails

logger = logging.getLogger('etradeFast.custom')
erp_api_url = 'http://114.67.231.162/api'
erp_app = '3123415742'
erp_secret = 'c3b5fee170b52b8397852c8ba03ef109'


# 查询订单, page默认500页, limit默认200且最大200
def trades(obj_stamp, page=500, limit=200):
    for page_no in range(1, page):
        # 请求入参
        erp_params = {
            "create_time": str(obj_stamp),
            "page": page_no,
            "limit": limit
        }
        erp_params = dict(init_system_params(), **erp_params)

        # 字典排序和MD5加密
        en_result = sort_dict_and_encryption_md5(erp_params)

        # 添加万里牛签名
        erp_params["_sign"] = en_result.hexdigest()

        # 接口请求
        erp_post_url = erp_api_url + '/erp/opentrade/query/trades'
        erp_r = requests.post(erp_post_url, json=erp_params)
        erp_result_object = erp_r.json()

        # 写日志
        logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

        # 写入数据库
        if "data" in erp_result_object and len(erp_result_object['data']) > 0:
            for dict_result_obj in erp_result_object['data']:
                trade = Trades()
                if "shop_name" in dict_result_obj.keys():
                    trade.shop_name = dict_result_obj['shop_name']
                if "shop_nick" in dict_result_obj.keys():
                    trade.shop_nick = dict_result_obj['shop_nick']
                if "storage_name" in dict_result_obj.keys():
                    trade.storage_name = dict_result_obj['storage_name']
                if "storage_code" in dict_result_obj.keys():
                    trade.storage_code = dict_result_obj['storage_code']
                if "trade_no" in dict_result_obj.keys():
                    trade.trade_no = dict_result_obj['trade_no']
                if "buyer_msg" in dict_result_obj.keys():
                    trade.buyer_msg = dict_result_obj['buyer_msg']
                if "seller_msg" in dict_result_obj.keys():
                    trade.seller_msg = dict_result_obj['seller_msg']
                if "oln_status" in dict_result_obj.keys():
                    trade.oln_status = dict_result_obj['oln_status']
                if "buyer_account" in dict_result_obj.keys():
                    trade.buyer_account = dict_result_obj['buyer_account']
                if "buyer" in dict_result_obj.keys():
                    trade.buyer = dict_result_obj['buyer']
                if "receiver" in dict_result_obj.keys():
                    trade.receiver = dict_result_obj['receiver']
                if "phone" in dict_result_obj.keys():
                    trade.phone = dict_result_obj['phone']
                if "country" in dict_result_obj.keys():
                    trade.country = dict_result_obj['country']
                if "province" in dict_result_obj.keys():
                    trade.province = dict_result_obj['province']
                if "city" in dict_result_obj.keys():
                    trade.city = dict_result_obj['city']
                if "district" in dict_result_obj.keys():
                    trade.district = dict_result_obj['district']
                if "address" in dict_result_obj.keys():
                    trade.address = dict_result_obj['address']
                if "create_time" in dict_result_obj.keys() and int(dict_result_obj['create_time']) > 0:
                    trade.create_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['create_time']) / 1000)
                if "modify_time" in dict_result_obj.keys() and int(dict_result_obj['modify_time']) > 0:
                    trade.modify_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['modify_time']) / 1000)
                if "send_time" in dict_result_obj.keys() and int(dict_result_obj['send_time']) > 0:
                    trade.send_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['send_time']) / 1000)
                if "pay_time" in dict_result_obj.keys() and int(dict_result_obj['pay_time']) > 0:
                    trade.pay_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['pay_time']) / 1000)
                if "end_time" in dict_result_obj.keys() and int(dict_result_obj['end_time']) > 0:
                    trade.end_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['end_time']) / 1000)
                if "status" in dict_result_obj.keys():
                    trade.status = dict_result_obj['status']
                if "is_pay" in dict_result_obj.keys():
                    trade.is_pay = dict_result_obj['is_pay']
                if "is_exception_trade" in dict_result_obj.keys():
                    trade.is_exception_trade = dict_result_obj['is_exception_trade']
                if "tp_tid" in dict_result_obj.keys():
                    trade.tp_tid = dict_result_obj['tp_tid']
                if "source_platform" in dict_result_obj.keys():
                    trade.source_platform = dict_result_obj['source_platform']
                if "sum_sale" in dict_result_obj.keys():
                    trade.sum_sale = dict_result_obj['sum_sale']
                if "post_fee" in dict_result_obj.keys():
                    trade.post_fee = dict_result_obj['post_fee']
                if "paid_fee" in dict_result_obj.keys():
                    trade.paid_fee = dict_result_obj['paid_fee']
                if "discount_fee" in dict_result_obj.keys():
                    trade.discount_fee = dict_result_obj['discount_fee']
                if "service_fee" in dict_result_obj.keys():
                    trade.service_fee = dict_result_obj['service_fee']
                if "has_refund" in dict_result_obj.keys():
                    trade.has_refund = dict_result_obj['has_refund']
                if "oln_order_list" in dict_result_obj.keys():
                    trade.oln_order_list = dict_result_obj['oln_order_list']
                if "is_small_trade" in dict_result_obj.keys():
                    trade.is_small_trade = dict_result_obj['is_small_trade']
                if "process_status" in dict_result_obj.keys():
                    trade.process_status = dict_result_obj['process_status']
                if "trade_type" in dict_result_obj.keys():
                    trade.trade_type = dict_result_obj['trade_type']
                if "mark" in dict_result_obj.keys():
                    trade.mark = dict_result_obj['mark']
                if "flag" in dict_result_obj.keys():
                    trade.flag = dict_result_obj['flag']
                if "pay_no" in dict_result_obj.keys():
                    trade.pay_no = dict_result_obj['pay_no']
                if "pay_type" in dict_result_obj.keys():
                    trade.pay_type = dict_result_obj['pay_type']
                if "currency_code" in dict_result_obj.keys():
                    trade.currency_code = dict_result_obj['currency_code']
                if "currency_sum" in dict_result_obj.keys():
                    trade.currency_sum = dict_result_obj['currency_sum']

                trade.save()

                if "orders" in dict_result_obj.keys() and len(dict_result_obj['orders']) > 0:
                    for dict_order_result_obj in dict_result_obj['orders']:
                        order = Orders()
                        order.trade_id = trade.trade_id
                        if "size" in dict_order_result_obj.keys():
                            order.size = dict_order_result_obj['size']
                        if "price" in dict_order_result_obj.keys():
                            order.price = dict_order_result_obj['price']
                        if "receivable" in dict_order_result_obj.keys():
                            order.receivable = dict_order_result_obj['receivable']
                        if "payment" in dict_order_result_obj.keys():
                            order.payment = dict_order_result_obj['payment']
                        if "tp_tid" in dict_order_result_obj.keys():
                            order.tp_tid = dict_order_result_obj['tp_tid']
                        if "oln_item_id" in dict_order_result_obj.keys():
                            order.oln_item_id = dict_order_result_obj['oln_item_id']
                        if "oln_status" in dict_order_result_obj.keys():
                            order.oln_status = dict_order_result_obj['oln_status']
                        if "oln_sku_id" in dict_order_result_obj.keys():
                            order.oln_sku_id = dict_order_result_obj['oln_sku_id']
                        if "status" in dict_order_result_obj.keys():
                            order.status = dict_order_result_obj['status']
                        if "orders_id" in dict_order_result_obj.keys():
                            order.orders_id = dict_order_result_obj['order_id']
                        if "oln_item_name" in dict_order_result_obj.keys():
                            order.oln_item_name = dict_order_result_obj['oln_item_name']
                        if "has_refund" in dict_order_result_obj.keys():
                            order.has_refund = dict_order_result_obj['has_refund']
                        if "tp_oid" in dict_order_result_obj.keys():
                            order.tp_oid = dict_order_result_obj['tp_oid']
                        if "is_gift" in dict_order_result_obj.keys():
                            order.is_gift = dict_order_result_obj['is_gift']

                        order.save()

        else:
            # 结束子循环
            break

    # 返回请求结果
    return True


# 查询库存 分页大小最大允许100
def inventory_item(modify_time, page_size=100):
    # 遍历目标仓库
    storage_filter_result = Storage.objects.filter(status=1)
    print("目标仓库数量: %d" % len(storage_filter_result))
    for storage in storage_filter_result:
        for page_no in range(1, 100):
            # 请求入参
            erp_params = {
                "modify_time": modify_time,
                "page_no": page_no,
                "page_size": page_size,
                "storage": storage.storage_code
            }
            erp_params = dict(init_system_params(), **erp_params)

            # 字典排序和MD5加密
            en_result = sort_dict_and_encryption_md5(erp_params)

            # 添加万里牛签名
            erp_params["_sign"] = en_result.hexdigest()

            # 接口请求
            erp_post_url = erp_api_url + '/erp/open/inventory/items/get/by/modifytime'
            erp_r = requests.post(erp_post_url, json=erp_params)
            erp_result_object = erp_r.json()

            # 写日志
            logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

            # 写入数据库
            if "data" in erp_result_object and len(erp_result_object['data']) > 0:
                for dict_result_obj in erp_result_object['data']:
                    inventory = Inventory()
                    inventory.storage_id = storage.storage_id

                    if "goods_code" in dict_result_obj.keys():
                        inventory.goods_code = dict_result_obj['goods_code']

                    inventory.storage_code = storage.storage_code

                    if "lock_size" in dict_result_obj.keys():
                        inventory.lock_size = dict_result_obj['lock_size']

                    if "quantity" in dict_result_obj.keys():
                        inventory.quantity = dict_result_obj['quantity']

                    if "sku_code" in dict_result_obj.keys():
                        inventory.sku_code = dict_result_obj['sku_code']

                    if "underway" in dict_result_obj.keys():
                        inventory.underway = dict_result_obj['underway']

                    # 检查库存商品是否已经存在, 存在的则进行更新
                    inventory_filter_result = Inventory.objects.filter(sku_code=inventory.sku_code)
                    if len(inventory_filter_result) > 0:
                        inventory_filter_result.lock_size = inventory.lock_size
                        inventory_filter_result.quantity = inventory.quantity
                        inventory_filter_result.underway = inventory.underway
                        inventory_filter_result.update()
                        print("update inventory")
                        # 赋值给子集合用
                        # inventory.inventory_id = inventory_filter_result.inventory_id
                        # continue
                    else:
                        # 写入
                        inventory.save()

                    # 删除原来的库存批次, 重新写入
                    Batches.objects.filter(inventory_id=inventory.inventory_id).delete()
                    if "batchs" in dict_result_obj.keys() and len(dict_result_obj['batchs']) > 0:
                        for dict_batches_result_obj in dict_result_obj['batchs']:
                            batches = Batches()
                            batches.inventory_id = inventory.inventory_id

                            if "batch_no" in dict_batches_result_obj.keys():
                                batches.batch_no = dict_batches_result_obj['batch_no']

                            if "expired_date" in dict_batches_result_obj.keys() and int(dict_batches_result_obj['expired_date']) > 0:
                                print("expired_date: %d" % dict_batches_result_obj['expired_date'])
                                batches.expired_date = timezone.datetime.utcfromtimestamp(int(dict_batches_result_obj['expired_date']) / 1000)

                            if "num" in dict_batches_result_obj.keys():
                                batches.num = dict_batches_result_obj['num']

                            if "produce_date" in dict_batches_result_obj.keys() and int(dict_batches_result_obj['produce_date']) > 0:
                                print("produce_date: %d" % dict_batches_result_obj['produce_date'])
                                batches.produce_date = timezone.datetime.utcfromtimestamp(int(dict_batches_result_obj['produce_date']) / 1000)

                            batches.save()

            else:
                # 结束子循环
                break

    # 返回请求结果
    return True


# 商品
# 查询商品信息
def item_goods_query():
    # 请求入参
    erp_params = {
        # "keyword": "",
        "page_no": 1,
        "page_size": 10,
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/item/goods/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 返回请求结果
    return erp_result_object


# 查询出商品并带有规格列表 spec_code,item_code,modify_time,bar_code至少一个不能为空  page默认100页, limit默认200且最大200
def goods_spec_list(modify_time, page=100, limit=200):
    for page_no in range(1, page):
        # 请求入参
        erp_params = {
            "modify_time": modify_time,
            "page": page_no,
            "limit": limit,
        }
        erp_params = dict(init_system_params(), **erp_params)

        # 字典排序和MD5加密
        en_result = sort_dict_and_encryption_md5(erp_params)

        # 添加万里牛签名
        erp_params["_sign"] = en_result.hexdigest()

        # 接口请求
        erp_post_url = erp_api_url + '/erp/goods/spec/open/query/goodswithspeclist'
        erp_r = requests.post(erp_post_url, json=erp_params)
        erp_result_object = erp_r.json()

        # 写日志
        logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

        # 写入数据库
        if "data" in erp_result_object and len(erp_result_object['data']) > 0:
            for dict_result_obj in erp_result_object['data']:
                goods = Goods()
                if "brand_name" in dict_result_obj.keys():
                    goods.brand_name = dict_result_obj['brand_name']

                if "catagory_name" in dict_result_obj.keys():
                    goods.category_name = dict_result_obj['catagory_name']

                if "expiration" in dict_result_obj.keys():
                    goods.expiration = dict_result_obj['expiration']

                if "goods_code" in dict_result_obj.keys():
                    goods.goods_code = dict_result_obj['goods_code']

                if "goods_name" in dict_result_obj.keys():
                    goods.goods_name = dict_result_obj['goods_name']

                if "manufacturer_name" in dict_result_obj.keys():
                    goods.manufacturer_name = dict_result_obj['manufacturer_name']

                if "pic" in dict_result_obj.keys():
                    goods.pic = dict_result_obj['pic']

                if "purchase_num" in dict_result_obj.keys():
                    goods.purchase_num = dict_result_obj['purchase_num']

                if "purchase_type_name" in dict_result_obj.keys():
                    goods.purchase_type_name = dict_result_obj['purchase_type_name']

                if "remark" in dict_result_obj.keys():
                    goods.remark = dict_result_obj['remark']

                if "tag_price" in dict_result_obj.keys():
                    goods.tag_price = dict_result_obj['tag_price']

                if "unit_name" in dict_result_obj.keys():
                    goods.unit_name = dict_result_obj['unit_name']

                # 检查商品是否已经存在, 存在的则进行更新
                goods_filter_result = Goods.objects.filter(goods_code=goods.goods_code)
                if len(goods_filter_result) > 0:
                    goods_filter_result.brand_name = goods.brand_name
                    goods_filter_result.catagory_name = goods.category_name
                    goods_filter_result.expiration = goods.expiration
                    goods_filter_result.goods_name = goods.goods_name
                    goods_filter_result.manufacturer_name = goods.manufacturer_name
                    goods_filter_result.pic = goods.pic
                    goods_filter_result.purchase_num = goods.purchase_num
                    goods_filter_result.purchase_type_name = goods.purchase_type_name
                    goods_filter_result.remark = goods.remark
                    goods_filter_result.tag_price = goods.tag_price
                    goods_filter_result.unit_name = goods.unit_name
                    goods_filter_result.update()
                    # continue
                else:
                    # 写入
                    goods.save()

                # 删除原来的商品规格, 重新写入
                GoodsSpecs.objects.filter(goods_code=goods.goods_code).delete()
                if "specs" in dict_result_obj.keys() and len(dict_result_obj['specs']) > 0:
                    for dict_specs_result_obj in dict_result_obj['specs']:
                        goods_specs = GoodsSpecs()
                        goods_specs.goods_id = goods.goods_id
                        goods_specs.goods_code = goods.goods_code
                        if "barcode" in dict_specs_result_obj.keys():
                            goods_specs.bar_code = dict_specs_result_obj['barcode']

                        if "spec_code" in dict_specs_result_obj.keys():
                            goods_specs.spec_code = dict_specs_result_obj['spec_code']

                        if "height" in dict_specs_result_obj.keys():
                            goods_specs.height = dict_specs_result_obj['height']

                        if "length" in dict_specs_result_obj.keys():
                            goods_specs.length = dict_specs_result_obj['length']

                        if "width" in dict_specs_result_obj.keys():
                            goods_specs.width = dict_specs_result_obj['width']

                        if "weight" in dict_specs_result_obj.keys():
                            goods_specs.weight = dict_specs_result_obj['weight']

                        if "pic" in dict_specs_result_obj.keys():
                            goods_specs.pic = dict_specs_result_obj['pic']

                        if "prime_price" in dict_specs_result_obj.keys():
                            goods_specs.prime_price = dict_specs_result_obj['prime_price']

                        if "sale_price" in dict_specs_result_obj.keys():
                            goods_specs.sale_price = dict_specs_result_obj['sale_price']

                        if "wholesale_price" in dict_specs_result_obj.keys():
                            goods_specs.wholesale_price = dict_specs_result_obj['wholesale_price']

                        if "spec1" in dict_specs_result_obj.keys():
                            goods_specs.spec1 = dict_specs_result_obj['spec1']

                        if "barcode" in dict_specs_result_obj.keys():
                            goods_specs.spec2 = dict_specs_result_obj['spec2']

                        goods_specs.save()

        else:
            # 结束子循环
            break

    # 返回请求结果
    return True


# 查询商品规格集合编码 spec_code,item_code,modify_time,bar_code 不能同时为空
def goods_spec_query(modify_time, page=1, limit=10):
    # 请求入参
    erp_params = {
        "modify_time": modify_time,
        "page": page,
        "limit": limit,
    }
    erp_params = dict(init_system_params(), ** erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/goods/spec/open/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 写入数据库
    if "data" in erp_result_object and len(erp_result_object['data']) > 0:
        for dict_result_obj in erp_result_object['data']:
            specs = Specs()
            if "bar_code" in dict_result_obj.keys():
                specs.bar_code = dict_result_obj['bar_code']
            if "item_name" in dict_result_obj.keys():
                specs.item_name = dict_result_obj['item_name']
            if "spec_code" in dict_result_obj.keys():
                specs.spec_code = dict_result_obj['spec_code']
            if "color" in dict_result_obj.keys():
                specs.color = dict_result_obj['color']
            if "price" in dict_result_obj.keys():
                specs.price = dict_result_obj['price']
            if "article_number" in dict_result_obj.keys():
                specs.article_number = dict_result_obj['article_number']
            if "item_code" in dict_result_obj.keys():
                specs.item_code = dict_result_obj['item_code']
            if "catagory" in dict_result_obj.keys():
                specs.category = dict_result_obj['catagory']
            if "brand" in dict_result_obj.keys():
                specs.brand = dict_result_obj['brand']
            if "other_prop" in dict_result_obj.keys():
                specs.other_prop = dict_result_obj['other_prop']
            if "unit" in dict_result_obj.keys():
                specs.unit = dict_result_obj['unit']
            if "prop1" in dict_result_obj.keys():
                specs.prop1 = dict_result_obj['prop1']
            if "prop2" in dict_result_obj.keys():
                specs.prop2 = dict_result_obj['prop2']
            if "prop3" in dict_result_obj.keys():
                specs.bar_code = dict_result_obj['prop3']

            specs.save()

    # 返回请求结果
    return erp_result_object


# 调拨接口
# 调拨入库单查询
def allocation_in_change_bill_query():
    # 当前日期3个月前时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=90)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 请求入参
    erp_params = {
        "modify_time": str(obj_stamp),
        "page": 1,
        "limit": 2
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/allocation/in/changebill/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 返回请求结果
    return erp_result_object


# 调拨出库单查询
def allocation_out_change_bill_query():
    # 当前日期3个月前时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=90)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 请求入参
    erp_params = {
        "modify_time": str(obj_stamp),
        "page": 1,
        "limit": 2
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/allocation/out/changebill/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 返回请求结果
    return erp_result_object


# storage 仓库接口, 测试数据有50间
def storage_query(page_no=1, page_size=10):
    # 请求入参
    erp_params = {
        "page_no": page_no,
        "page_size": page_size
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/base/storage/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 写入数据库
    if "data" in erp_result_object and len(erp_result_object['data']) > 0:
        for dict_result_obj in erp_result_object['data']:
            erp_storage = Storage()
            if "storage_code" in dict_result_obj.keys():
                erp_storage.storage_code = dict_result_obj['storage_code']
            if "storage_name" in dict_result_obj.keys():
                erp_storage.storage_name = dict_result_obj['storage_name']
            if "status" in dict_result_obj.keys():
                erp_storage.status = dict_result_obj['status']

            # 检查仓库是否已经存在, 存在的则进行更新
            storage_filter_result = Storage.objects.filter(storage_code=erp_storage.storage_code)
            if len(storage_filter_result) > 0:
                storage_filter_result.storage_name = erp_storage.storage_name
                storage_filter_result.status = erp_storage.status
                storage_filter_result.update()
                # continue
            else:
                # 写入
                erp_storage.save()

    # 返回请求结果
    return erp_result_object


# 查询销售/线下出库单
def sale_stock_out_query(modify_time, page=200, limit=10):
    for page_no in range(1, page):
        # 请求入参
        erp_params = {
            "modify_time": modify_time,
            "page": page_no,
            "limit": limit
        }
        erp_params = dict(init_system_params(), **erp_params)

        # 字典排序和MD5加密
        en_result = sort_dict_and_encryption_md5(erp_params)

        # 添加万里牛签名
        erp_params["_sign"] = en_result.hexdigest()

        # 接口请求
        erp_post_url = erp_api_url + '/erp/sale/stock/out/query'
        erp_r = requests.post(erp_post_url, json=erp_params)
        erp_result_object = erp_r.json()

        # 写日志
        logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

        # 写入数据库
        if "data" in erp_result_object and len(erp_result_object['data']) > 0:
            for dict_result_obj in erp_result_object['data']:
                sale_stock = SaleStock()
                if "bill_date" in dict_result_obj.keys() and int(dict_result_obj['bill_date']) > 0:
                    sale_stock.bill_date = timezone.datetime.utcfromtimestamp(int(dict_result_obj['bill_date']) / 1000)

                if "bill_type" in dict_result_obj.keys():
                    sale_stock.bill_type = dict_result_obj['bill_type']

                if "country" in dict_result_obj.keys():
                    sale_stock.country = dict_result_obj['country']

                if "create_time" in dict_result_obj.keys() and int(dict_result_obj['create_time']) > 0:
                    sale_stock.create_time = timezone.datetime.utcfromtimestamp(int(dict_result_obj['create_time']) / 1000)

                if "custom_code" in dict_result_obj.keys():
                    sale_stock.custom_code = dict_result_obj['custom_code']

                if "custom_name" in dict_result_obj.keys():
                    sale_stock.custom_name = dict_result_obj['custom_name']

                if "customer_nick" in dict_result_obj.keys():
                    sale_stock.customer_nick = dict_result_obj['customer_nick']

                if "customer_nick_type" in dict_result_obj.keys():
                    sale_stock.customer_nick_type = dict_result_obj['customer_nick_type']

                if "customer_nick_type_name" in dict_result_obj.keys():
                    sale_stock.customer_nick_type_name = dict_result_obj['customer_nick_type_name']

                if "discount_fee" in dict_result_obj.keys():
                    sale_stock.discount_fee = dict_result_obj['discount_fee']

                if "from_trade_no" in dict_result_obj.keys():
                    sale_stock.from_trade_no = dict_result_obj['from_trade_no']

                if "inv_no" in dict_result_obj.keys():
                    sale_stock.inv_no = dict_result_obj['inv_no']

                if "paid_fee" in dict_result_obj.keys():
                    sale_stock.paid_fee = dict_result_obj['paid_fee']

                if "post_fee" in dict_result_obj.keys():
                    sale_stock.post_fee = dict_result_obj['post_fee']

                if "remark" in dict_result_obj.keys():
                    sale_stock.remark = dict_result_obj['remark']

                if "sale_man" in dict_result_obj.keys():
                    sale_stock.sale_man = dict_result_obj['sale_man']

                if "service_fee" in dict_result_obj.keys():
                    sale_stock.service_fee = dict_result_obj['service_fee']

                if "shop_name" in dict_result_obj.keys():
                    sale_stock.shop_name = dict_result_obj['shop_name']

                if "shop_nick" in dict_result_obj.keys():
                    sale_stock.shop_nick = dict_result_obj['shop_nick']

                if "shop_source" in dict_result_obj.keys():
                    sale_stock.shop_source = dict_result_obj['shop_source']

                if "storage_code" in dict_result_obj.keys():
                    sale_stock.storage_code = dict_result_obj['storage_code']

                if "sum_sale" in dict_result_obj.keys():
                    sale_stock.sum_sale = dict_result_obj['sum_sale']

                if "tp_tid" in dict_result_obj.keys():
                    sale_stock.tp_tid = dict_result_obj['tp_tid']

                # 检查出库单是否存在, 存在的则跳过
                sale_stock_filter_result = SaleStock.objects.filter(inv_no=sale_stock.inv_no)
                if len(sale_stock_filter_result) > 0:
                    continue
                else:
                    sale_stock.save()

                    if "details" in dict_result_obj.keys() and len(dict_result_obj['details']) > 0:
                        for dict_sale_stock_details_result_obj in dict_result_obj['details']:
                            sale_stock_detail = SaleStockDetails()
                            sale_stock_detail.sale_stock_id = sale_stock.sale_stock_id

                            if "goods_name" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.goods_name = dict_sale_stock_details_result_obj['goods_name']

                            if "discount_fee" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.discount_fee = dict_sale_stock_details_result_obj['discount_fee']

                            if "nums" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.nums = dict_sale_stock_details_result_obj['nums']

                            if "sum_cost" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sum_cost = dict_sale_stock_details_result_obj['sum_cost']

                            if "sum_sale" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sum_sale = dict_sale_stock_details_result_obj['sum_sale']

                            if "sku_name" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sku_name = dict_sale_stock_details_result_obj['sku_name']

                            if "sku_no" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sku_no = dict_sale_stock_details_result_obj['sku_no']

                            if "sku_prop1" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sku_prop1 = dict_sale_stock_details_result_obj['sku_prop1']

                            if "sku_prop2" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.sku_prop2 = dict_sale_stock_details_result_obj['sku_prop2']

                            if "unit" in dict_sale_stock_details_result_obj.keys():
                                sale_stock_detail.unit = dict_sale_stock_details_result_obj['unit']

                            sale_stock_detail.save()

        else:
            # 结束子循环
            break

    # 返回请求结果
    return True


# purchase 采购接口
# 查询采购订单 bill_code modify_time 不能同时为空
def purchase_query():
    # 当前日期3个月前时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=90)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 请求入参
    erp_params = {
        "modify_time": str(obj_stamp),
        "page": 1,
        "limit": 2
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/purchase/purchasebill/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 返回请求结果
    return erp_result_object


# supplier 查询供应商信息
def supplier_query(page_no=1, page_size=10):
    # 请求入参
    erp_params = {
        "page_no": page_no,
        "page_size": page_size
    }
    erp_params = dict(init_system_params(), **erp_params)

    # 字典排序和MD5加密
    en_result = sort_dict_and_encryption_md5(erp_params)

    # 添加万里牛签名
    erp_params["_sign"] = en_result.hexdigest()

    # 接口请求
    erp_post_url = erp_api_url + '/erp/base/supplier/query'
    erp_r = requests.post(erp_post_url, json=erp_params)
    erp_result_object = erp_r.json()

    # 写日志
    logger.debug(erp_post_url + '\r\n' + str(erp_params) + '\r\n' + str(erp_result_object) + '\r\n')

    # 写入数据库
    if "data" in erp_result_object and len(erp_result_object['data']) > 0:
        for dict_result_obj in erp_result_object['data']:
            supplier = Supplier()
            if "supplier_code" in dict_result_obj.keys():
                supplier.supplier_code = dict_result_obj['supplier_code']
            if "supplier_name" in dict_result_obj.keys():
                supplier.supplier_name = dict_result_obj['supplier_name']
            if "status" in dict_result_obj.keys():
                supplier.status = dict_result_obj['status']

            # 检查供应商是否已经存在, 存在的则进行更新
            supplier_filter_result = Supplier.objects.filter(supplier_code=supplier.supplier_code)
            if len(supplier_filter_result) > 0:
                supplier_filter_result.supplier_name = supplier.supplier_name
                supplier_filter_result.status = supplier.status
                supplier_filter_result.update()
            else:
                # 写入
                supplier.save()

    # 返回请求结果
    return erp_result_object


# 用 MD5 加密
def sort_dict_and_encryption_md5(erp_params):
    # 字典排序
    refresh_params = dict([(k, erp_params[k]) for k in sorted(erp_params.keys())])
    refresh_b = refresh_params.items()
    refresh_list = []
    for key, value in refresh_b:
        s3 = "%s=%s" % (key, value)
        refresh_list.append(s3)

    # MD5加密
    en_result = hashlib.md5()
    # 待加密信息
    source_md5 = erp_secret + "&".join(refresh_list) + erp_secret
    en_result.update(source_md5.encode(encoding='utf-8'))

    print(source_md5)
    return en_result


# 初始化系统入参
def init_system_params():
    # 当前时间戳
    now_timestamp = time.time()
    system_params = {
        "_app": erp_app,
        "_t": int(now_timestamp),
        "_s": ''
    }
    return system_params
