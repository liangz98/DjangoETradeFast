from django.urls import path

from . import views

# app_name 设置命名空间, 用于 Django 分辨重名的URL
app_name = 'helloWorld'
urlpatterns = [
    # 首页
    path('', views.index, name='index'),
    # 查看
    path('view/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/<int:year>/', views.detail, name='detail'),
    # 新增
    path('add_hello_world/', views.add_hello_world, name='add'),
    path('add_hello_world_save/', views.add_hello_world_save, name='addSave'),

    # 使用模板
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
