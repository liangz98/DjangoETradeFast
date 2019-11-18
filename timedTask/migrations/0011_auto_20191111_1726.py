# Generated by Django 2.2.1 on 2019-11-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timedTask', '0010_auto_20191111_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='tag_price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='吊牌价'),
        ),
        migrations.AddField(
            model_name='goods',
            name='unit_name',
            field=models.CharField(max_length=128, null=True, verbose_name='单位'),
        ),
    ]
