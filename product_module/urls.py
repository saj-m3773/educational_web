from django.urls import path, re_path
from product_module import views

urlpatterns = [
               path('', views.ProductListView.as_view(), name='product'),
               re_path(r'(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product-d'),
               path('add_product_comment', views.add_product_comment, name='add_product_comment')

               ]
