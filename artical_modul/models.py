from User_module.models import User
from django.db import models
from jalali_date import date2jalali


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'


class ArticaleTag(models.Model):
    coption = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    slug = models.SlugField(verbose_name='عنوتن url', unique=True, db_index=True, allow_unicode=True)
    is_activ = models.BooleanField(verbose_name='فعال /غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'تگ مقاله'
        verbose_name_plural = 'تگ های مقاله'

    def __str__(self):
        return self.coption


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه', max_length=100)
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی ها')
    tags = models.ManyToManyField(ArticaleTag, verbose_name='تگ ها',related_name='articales')

    # نویسنده کیست؟
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)
    create_data = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_data)

    def get_jalali_create_time(self):
        return self.create_data.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    is_active = models.BooleanField(default=False, verbose_name='تایید / عدم تایید')

    class Meta:
        verbose_name = 'نطر مقاله'
        verbose_name_plural = 'نظرات مقاله'
