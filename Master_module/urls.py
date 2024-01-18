from django.urls import path,re_path

from . import views

urlpatterns = [

    path('',views.MasterListView.as_view(),name='master'),
    re_path(r'(?P<pk>[-\w]+)/', views.Master_profileDetailView.as_view(), name='master_profile'),
]
