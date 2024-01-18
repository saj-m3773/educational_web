# Generated by Django 4.2.7 on 2023-12-28 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(verbose_name='نهایی شده/نشده')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبدهای خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pay', models.BooleanField(verbose_name='خریداری شده/نشده')),
                ('final_price', models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_modul.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزییات سبد خرید',
                'verbose_name_plural': 'لیست جزییات سبدهای خرید',
            },
        ),
    ]
