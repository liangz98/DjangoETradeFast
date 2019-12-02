import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from timedTask.erpApi import storage_query, trades, inventory_item, goods_spec_list
# from timedTask.models import Person


# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')

# # 每天8点半执行这个任务
# @register_job(scheduler, 'cron', id='test', hour=8, minute=30)
# def test(s):
#     # 具体要执行的代码
#     pass

# 每天凌晨1点执行
@register_job(scheduler, 'cron', id='erp_storage_query', hour=1)
def get_erp_storage_query():
    print("Start --- timedTask! hour=1 erp_storage_query")
    # 仓库数据
    storage_query(1, 100)
    print("end --- timedTask! success!!")


@register_job(scheduler, 'cron', id='erp_trades', hour=1, minute=5)
def get_erp_trades():
    print("Start --- timedTask! hour=1 erp_trades")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询订单数据
    trades(obj_stamp)
    print("end --- timedTask! success!!")


@register_job(scheduler, 'cron', id='erp_inventory', hour=1, minute=15)
def get_erp_inventory():
    print("Start --- timedTask! hour=1 erp_inventory")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询库存数据
    inventory_item(obj_stamp)
    print("end --- timedTask! success!!")


@register_job(scheduler, 'cron', id='erp_goods', hour=1, minute=25)
def get_erp_goods():
    print("Start --- timedTask! hour=1 erp_goods")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询出商品并带有规格列表
    goods_spec_list(obj_stamp)
    print("end --- timedTask! success!!")


# 每天中午12点半执行
@register_job(scheduler, 'cron', id='erp_storage_pm_1200', hour=12)
def get_erp_storage_pm():
    print("Start --- timedTask! hour=PM 12:00 erp_storage_pm_1200")
    # 仓库数据
    storage_query(1, 100)
    print("end --- timedTask! hour=PM 12:00 success!!")


@register_job(scheduler, 'cron', id='erp_trades_pm_1200', hour=12, minute=5)
def get_erp_trades_pm():
    print("Start --- timedTask! hour=PM 12:05 erp_trades_pm_1200")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询订单数据
    trades(obj_stamp)
    print("end --- timedTask! hour=PM 12:05 success!!")


@register_job(scheduler, 'cron', id='erp_inventory_pm_1200', hour=12, minute=15)
def get_erp_inventory_pm():
    print("Start --- timedTask! hour=PM 12:15 erp_inventory_pm_1200")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询库存数据
    inventory_item(obj_stamp)
    print("end --- timedTask! hour=PM 12:15 success!!")


@register_job(scheduler, 'cron', id='erp_goods_pm_1200', hour=12, minute=25)
def get_erp_goods_pm():
    print("Start --- timedTask! hour=PM 12:25 erp_goods_pm_1200")
    # 当前日期前一天的时间戳
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=3)
    obj_stamp = int(then.timestamp() * 1000.0)

    # 查询出商品并带有规格列表
    goods_spec_list(obj_stamp)
    print("end --- timedTask! hour=PM 12:25 success!!")


# @register_job(scheduler, 'interval', id='test_timed', seconds=10)
# def timed_task_job():
#     print("I'm a test job --- timedTask! seconds=10")
#
#
# @register_job(scheduler, 'interval', id='test_1', seconds=20)
# def hello_world_job():
#     print("I'm a test job --- helloWorld! seconds=20")
#     person = Person(first_name='Bob', last_name='Lee')
#     person.save()
#
#
# @register_job(scheduler, 'interval', id='test_polls', minutes=1)
# def polls_job():
#     print("I'm a test job --- polls! minutes=1")
#     Person.objects.all().delete()


# 注册定时任务并开始
register_events(scheduler)
# scheduler.add_job(test_job, 'interval', seconds=5)
scheduler.start()
print("Scheduler started!")
