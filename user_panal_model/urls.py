from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='dashboard'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('email', views.EmailView.as_view(), name='email_page'),
    path('activate-account/<email_active_code>', views.ActivateEmailView.as_view(), name='activate_emmail'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('my-shopping', views.MyShopping.as_view(), name='user_shopping_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail'),
    path('my-shopping-detail/<order_id>', views.my_shopping_detail, name='user_shopping_detail_page'),
    path('my-terning', views.my_terning, name='user_terning'),

]
