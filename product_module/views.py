from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from order_modul.models import OrderDetail
from product_module.models import Product, ProductCategory, ProductVisit, File, ProductComment
from site_module.models import SiteBanner
from utils.convarter import group_list_product
from utils.http_servis import get_client_ip


class ProductListView(ListView):
    template_name = 'propduct/product_list.html'
    model = Product
    ordering = ['-id']
    paginate_by = 20  
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.product_list)
        return context


class ProductDetailView(DetailView):
    template_name = 'propduct/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        loaded_product = self.object

        product: Product = kwargs.get('object')

        context['comments'] = ProductComment.objects.filter(article_id=product.id, parent=None).prefetch_related(
            'productcomment_set')

        request = self.request
        favorite_product_id = request.session.get("protuct_fevorics")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        Files_product = list(File.objects.filter(product_id=loaded_product.id).all())
        context['Filess'] = group_list_product(Files_product)
        order = OrderDetail.objects.filter(product_id=product.id, order__user_id=request.user.id).first()
        context['order'] = order
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.product_detail)
        user_ip = get_client_ip(self.request)
        user_id = 0
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip)
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
        return context


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_activ=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'propduct/product_categories_component.html', context)


def add_product_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = ProductComment(article_id=article_id, text=article_comment, User_id=request.user.id,
                                     parent_id=parent_id, is_active=True)
        new_comment.save()
        context = {
            'comments': ProductComment.objects.filter(article_id=article_id, parent=None, is_active=True).order_by(
                '-create_date').prefetch_related('productcomment_set'),
            'comments_count': ProductComment.objects.filter(article_id=article_id).count()
        }

        return render(request, 'inclod/product_comment.html', context)

    return JsonResponse({
        'status': 'success',
        'text': ' نظر شما پس از تایید نمایش داده می شود',
        'confirm_button_text': 'باشه ممنونم',
        'icon': 'success'
    })
