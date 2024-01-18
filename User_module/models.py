from django.contrib.auth.models import AbstractUser
from django.db import models

from User_module.UserManagers import userManagers


class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    is_activeEmail = models.BooleanField(default=False, verbose_name='ایمیل فعال',)
    short_descriptio = models.CharField(max_length=80, db_index=True, blank=True, verbose_name='توضیحات کوتاه')
    about_user = models.TextField(null=True, verbose_name='درباره شخص')
    mobile = models.CharField(max_length=11, unique=True)
    Resume_Link = models.CharField(max_length=120, verbose_name='لینک رزومه', blank=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    objects = userManagers()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []  # چیزی اجباری نباشد

    backend = 'User_module.Backend.MobileBackend'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email
