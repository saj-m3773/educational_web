import datetime
import time
from kavenegar import *

from User_module import models
from Site_Work.settings import Kavenegar_API
from random import randint


def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '10008663',  # optional
            'receptor': mobile,  # multiple mobile number, split by comma
            'message': '{}'.format(otp),
        }
        response = api.sms_send(params)
        print("otp:", otp)


    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)


# time
def check_otp(mobile):
    try:
        user = models.User.objects.get(mobile=mobile)
        now =datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print('OTP TIME: ', diff_time)

        if diff_time.seconds > 120:
            return False
        return True

    except models.User.DoesNotExist:
        return False
