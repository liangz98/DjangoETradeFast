# Generated by Django 2.2.1 on 2019-11-08 15:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0005_goodsspec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('storage_code', models.CharField(max_length=256, null=True, verbose_name='仓库编码')),
                ('storage_name', models.CharField(max_length=256, null=True, verbose_name='仓库名称')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
            ],
        ),
    ]
