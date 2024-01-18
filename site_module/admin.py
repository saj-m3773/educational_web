from django.contrib import admin
from . import models


class FoterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'position']


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider)
admin.site.register(models.FooterLink, FoterLinkAdmin)
admin.site.register(models.SiteBanner, SiteBannerAdmin)
admin.site.register(models.SocialNetworks)
