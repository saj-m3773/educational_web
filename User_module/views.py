from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from User_module import forms, send
from User_module.models import User
from django.contrib import messages


def register_view(request):
    form = forms.RegisterForms

    # ثبت نام و ورود یکی باشد
    if request.method == 'POST':
        try:
            if "mobile" in request.POST:
                mobile = (request.POST.get('mobile'))
                print(mobile)
                user = User.objects.get(mobile=mobile)
                # send otp
                otp = send.get_random_otp()
                send.send_otp(mobile, otp)
                # save otp
                user.otp = otp
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify_user'))
                # اگر پیدا نکرد
        except User.DoesNotExist:
            # ثبت نام می کند
            form = forms.RegisterForms(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                # send otp
                otp = send.get_random_otp()
                send.send_otp(mobile, otp)
                # save otp
                user.otp = otp
                user.is_active = False
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify_user'))
                # redirect to verify page

    return render(request, 'Request.html', {'form': form})


def verify_user(request):
    try:
        mobile = request.session.get('user_mobile')

        user = User.objects.get(mobile=mobile)
        if request.method == "POST":  # اگر کاربر اطلاعات را وارد کرد
            # chack otp expiration
            if not send.check_otp(user.mobile):
                messages.error(request,'توکن منقضی شده است')
                return HttpResponseRedirect(reverse('register'))
            if user.otp != int(request.POST.get('otp')):
                messages.error(request, 'کد اشتباه است ,دوباره تلاش کنید')
                return HttpResponseRedirect(reverse('verify_user'))
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, 'verify.html', {'mobiles': mobile})
    except User.DoesNotExist:
        messages.error(request, 'خطا رخ داده است ,دوباره تلاش کنید')
        return HttpResponseRedirect(reverse('register'))


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('register'))
