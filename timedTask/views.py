from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from timedTask.models import Person


# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')

# # 每天8点半执行这个任务
# @register_job(scheduler, 'cron', id='test', hour=8, minute=30)
# def test(s):
#     # 具体要执行的代码
#     pass


@register_job(scheduler, 'interval', id='test_timed', seconds=10)
def timed_task_job():
    print("I'm a test job --- timedTask! seconds=10")


@register_job(scheduler, 'interval', id='test_1', seconds=20)
def hello_world_job():
    print("I'm a test job --- helloWorld! seconds=20")
    person = Person(first_name='Adom', last_name='Lee')
    person.save()


@register_job(scheduler, 'interval', id='test_polls', minutes=1)
def polls_job():
    print("I'm a test job --- polls! minutes=1")
    Person.objects.all().delete()


# 注册定时任务并开始
register_events(scheduler)
# scheduler.add_job(test_job, 'interval', seconds=5)
scheduler.start()
print("Scheduler started!")
