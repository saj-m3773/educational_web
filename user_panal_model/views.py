from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView
from User_module.models import User
from order_modul.models import Order, OrderDetail
from user_panal_model.forms import EditProfileModelForm, EmailForms
from utils.email_serves import send_email


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'dashbord.html'


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)

        context = {
            'form': edit_form, 'user': current_user
        }
        return render(request, 'edit_profile.html', context)

    def post(self, request: HttpRequest):
       
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form, 'user': current_user
        }

        return render(request, 'dashbord.html', context)


@method_decorator(login_required, name='dispatch')
class MyShopping(ListView):
    model = Order
    template_name = 'user_shopping.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(user_id=request.user.id, is_paid=True)
        return queryset


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_basket.html', context)


def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                             order__user_id=request.user.id).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_basket_content.html', context)
    })


def my_shopping_detail(request: HttpRequest, order_id):
    order = Order.objects.prefetch_related('orderdetail_set').filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('سبد خرید مورد نظر یافت نشد')

    return render(request, 'user_shopping_detail.html', {
        'order': order
    })


def my_terning(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').filter(is_paid=True,
                                                                                      user_id=request.user.id)
    context = {
        'order': created,

    }
    return render(request, 'MyTerning.html', context)


class EmailView(View):
    def get(self, request):
        Email_Forms = EmailForms()
        context = {
            'register_form': Email_Forms
        }

        return render(request, 'dashbord.html', context)

    def post(self, request):
        register_form = EmailForms(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user: User = User.objects.filter(is_active=True, id=request.user.id).first()
            users: bool = User.objects.filter(email__iexact=user_email).exists()
            if users:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                user.email = user_email
                user.email_active_code = get_random_string(72)
                user.is_activeEmail = False
                user.save()
                send_email('فعالسازی ایمیل کاربری', user.email, {'user': user}, 'emails/activate_account.html')
                return redirect(reverse('home_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'register.html', context)


class ActivateEmailView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if not user.is_activeEmail:
            user.is_activeEmail = True
            user.email_active_code = get_random_string(72)
            user.save()
            # todo: show success message to user
            return redirect(reverse('register'))
        else:

            pass
