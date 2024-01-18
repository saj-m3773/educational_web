from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')


    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title

class SocialNetworks(models.Model):
    title = models.CharField(max_length=200, verbose_name='شبکه اجتماعی')
    url = models.URLField(max_length=500, verbose_name='لینک')

    class Meta:
        verbose_name = 'دسته بندی شبکه اجتماعی'
        verbose_name_plural = 'دسته بندی های شبکه اجتماعی'

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=220, verbose_name='عنوان')
    url = models.CharField(max_length=200, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر ')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    images=models.ImageField(upload_to='images/slider',verbose_name="تصویر",null=True)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title



class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product', 'صفحه لیست محصولات',
        product_detail = 'product_d', 'صفحه ی جزییات محصولات',
        about_us = 'about_page', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name="نام بنر")
    url_title = models.URLField(max_length=400, null=True, verbose_name='url')
    image = models.ImageField(upload_to='images/banner', verbose_name='تصویر بنر')
    is_active = models.BooleanField(verbose_name='فعال است')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices,
                                verbose_name='موقیعت')  # در کدام صفحه باشد.

    # choices --> 1 list , admin az list antejab mokonad

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'
