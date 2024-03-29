# Generated by Django 4.2.7 on 2023-12-28 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='عنوان')),
                ('images', models.ImageField(null=True, upload_to='images/product', verbose_name='تصویر محصول')),
                ('base_File', models.FileField(blank=True, upload_to='product/File')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='استاد')),
            ],
            options={
                'verbose_name': 'محصولات',
                'verbose_name_plural': 'تمامی محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنواان در url ')),
                ('is_activ', models.BooleanField(verbose_name='فعال /غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='آی پی کاربر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدید های محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coption', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('is_activ', models.BooleanField(verbose_name='فعال /غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='مقاله')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productcomment', verbose_name='والد')),
            ],
            options={
                'verbose_name': 'نطرآموزش ',
                'verbose_name_plural': 'نظرات آموزش ها',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory', verbose_name='دسته بندی ها'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='نام ویدیو')),
                ('File', models.FileField(upload_to='product/File')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'فایل',
                'verbose_name_plural': 'فایل ها',
            },
        ),
    ]
