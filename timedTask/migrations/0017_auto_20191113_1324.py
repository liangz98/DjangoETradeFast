# Generated by Django 2.2.1 on 2019-11-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0016_auto_20191113_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='trade_no',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
