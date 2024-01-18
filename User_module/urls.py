from django.urls import path

from User_module import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('verify_user/', views.verify_user, name='verify_user'),
    path('loginout/', views.logoutView.as_view(), name='loginout'),
]
