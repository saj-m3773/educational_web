def my_callback(sender,**kwargs):
    print("Request finished")


#هرکاربر ثبت نام کرد بیاد برای ادمین

def create_news_user(sender,instance,created,**kwargs):
    if created:
        print("new user",instance)

def update_user(sender,instance,created,**kwargs):
    if created:
        print("update user",instance)

