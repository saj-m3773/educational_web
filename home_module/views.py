from django.db.models import Count, Sum
from django.shortcuts import render
from django.views.generic import TemplateView

from artical_modul.models import Article
from product_module.models import Product
from site_module.models import SiteSetting, FooterLinkBox, SocialNetworks, Slider


class HomeView(TemplateView):
    template_name = 'Home/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:20]
        context['latest_products'] = latest_products
        latest_article = Article.objects.filter(is_active=True).order_by('-id')[:10]
        context['latest_articles'] = latest_article
        most_visit_products = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:10]
        context['most_visit_products'] = most_visit_products

        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }

    return render(request, 'Home/SiteHader.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    foter_link_boxs = FooterLinkBox.objects.all()
    SocialNetwork = SocialNetworks.objects.all()

    context = {
        'site_setting': setting,
        'foter_linj_boxs': foter_link_boxs,
        'SocialNetworks': SocialNetwork

    }
    return render(request, 'Home/SiteFoter.html', context)


class AboutView(TemplateView):
    template_name = 'Home/About_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        Social_Networks: SocialNetworks = SocialNetworks
        context['site_setting'] = site_setting
        context['SocialNetworks'] = Social_Networks.objects.all()
        return context
