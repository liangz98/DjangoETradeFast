import datetime
import hashlib
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
import requests
import logging

from timedTask.erpApi import trades, inventory_item, item_goods_query, allocation_in_change_bill_query, allocation_out_change_bill_query, purchase_query, goods_spec_query, storage_query, supplier_query, goods_spec_list, sale_stock_out_query
from timedTask.models import Trades, Orders, Specs, Storage, GoodsSpecs, Goods, SaleStockDetails, SaleStock

logger = logging.getLogger('etradeFast.custom')


def index(request):
    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key

    headers = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Etrade_PhpAgent',
        'Authorization': 'MbMv1uuJWsufm5cA2GEU'
    }

    request_object = {
        "lang": "zh_CN",
        "userID": '',
        "sessionID": session_id,
        "accountID": '',
        "contactPreference": '',
        "timeZone": "GMT +8:00",
        "client": "121.33.145.180"
    }

    params = {
        'requestObject': request_object,
        'loginName': 'chris@baixing.com',
        'password': '123qazwsx',
        'authCode': ''
    }

    post_url = 'http://123.207.120.251:8080/phpapi/contactapi/contactApi!login.action'

    r = requests.post(post_url, headers=headers, json=params)
    result_object = r.json()

    logger.debug(post_url + '\r\n' + str(params) + '\r\n' + str(result_object) + '\r\n')
    # logger.debug('请求地址: ' + post_url + ' \r\n请求数据: ' + str(params))

    # 删除数据库
    # 订单
    # Trades.objects.all().delete()
    # Orders.objects.all().delete()

    # 规格
    # Specs.objects.all().delete()

    # 商品&商品格
    # GoodsSpecs.objects.all().delete()
    # Goods.objects.all().delete()

    # 仓库
    # Storage.objects.all().delete()

    # 销售/线下出库单
    # SaleStockDetails.objects.all().delete()
    # SaleStock.objects.all().delete()

    # 当前日期3个月前时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=2)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询供应商
    # erp_supplier_result_object = supplier_query(1, 10)

    # 查询商品
    # print("item_goods_query")
    # erp_item_goods_result_object = item_goods_query()

    # 查询商品规格
    # erp_goods_spec_result_object = goods_spec_query(obj_stamp, 1, 10)
    # print(len(erp_goods_spec_result_object['data']))

    # 调拨入库单查询
    # erp_allocation_in_result_object = allocation_in_change_bill_query()

    # 调拨出库单查询
    # erp_allocation_out_result_object = allocation_out_change_bill_query()

    # 查询采购订单
    # erp_purchase_result_object = purchase_query()

    # 查询销售/线下出库单
    # erp_sale_stock_result_object = sale_stock_out_query(obj_stamp)

    # ==============================================================================================
    # 已初始化的数据
    # 查询仓库
    # erp_storage_result_object = storage_query(1, 100)

    # 查询订单
    # erp_result_object = trades(obj_stamp)

    # 查询库存
    # print("inventory_item")
    erp_inventory_result_object = inventory_item(obj_stamp)

    # 查询出商品并带有规格列表
    # print("goods_spec_list")
    # erp_goods_spec_list_result_object = goods_spec_list(obj_stamp)

    # template = loader.get_template('helloWorld/index')
    context = {
        'bodyContent': "Hello, world. You're at the HelloWorld index.",
        'hello': 'Hello World!',
        'timeZone': timezone.now(),
        'session_key': request.session.session_key,
        'status': result_object['result'],
        'template_include_type': 'simple'
    }

    return render(request, 'helloWorld/index.html', context)


def detail(request, question_id='', year=0):
    context = {
        'bodyContent': "Hello, Detail. You're at the HelloWorld detail.",
        'hello': 'Hello Detail!',
        'id': question_id,
        'year': year
    }
    return render(request, 'helloWorld/detail.html', context)


def add_hello_world(request):
    # add_hello_world
    context = {

    }
    return render(request, 'helloWorld/add.html', context)


def add_hello_world_save(request):
    # 检查表单提交的内容, 如果缺少必须的值, 触发 KeyError 重新显示表单和一个错误信息
    try:
        name = request.POST['name']
    except KeyError:
        return render(request, 'helloWorld/add.html', {
            'error_message': 'Key 没有提交.'
        })
    else:
        # 处理提交的内容

        # 成功处理 POST 数据后，应始终返回 HttpResponseRedirect。
        return HttpResponseRedirect(reverse('helloWorld:detail', args=(name,)))
