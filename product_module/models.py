from django.db import models
from User_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='عنواان در url ', db_index=True)
    is_activ = models.BooleanField(verbose_name='فعال /غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):  # لحظه نمایش چه چیزی باشد
        return f"{self.title} "

    # چه چیزی نمایش داده شود
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=250, db_index=True, verbose_name='عنوان')
    images = models.ImageField(upload_to='images/product', null=True, verbose_name="تصویر محصول")
    category = models.ForeignKey(ProductCategory, verbose_name='دسته بندی ها', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')  # namaesh dade shavad or not
    slug = models.SlugField(null=False, max_length=100, blank=True, unique=True, db_index=True,
                            allow_unicode=True, verbose_name='عنوان در url')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده',default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='استاد', null=True, editable=False)

    def __str__(self):
        return f"{self.title} ({self.id})"

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'تمامی محصولات'


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    title = models.CharField(verbose_name="نام ویدیو", max_length=80)
    File = models.FileField(upload_to='product/File')

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل ها'

    def __str__(self):
        return self.title


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title}/{self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class ProductComment(models.Model):
    article = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ProductComment', null=True, on_delete=models.CASCADE, verbose_name='والد', blank=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    is_active = models.BooleanField(default=False, verbose_name='تایید / عدم تایید')

    class Meta:
        verbose_name = 'نطرآموزش '
        verbose_name_plural = 'نظرات آموزش ها'
