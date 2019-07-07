import os
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE'] = 'mproject.settings'
def sendmail(b,c):
    send_mail(
        '您的注册邮箱验证码',
        '邮箱验证码：'+b,
        '17319366584@sina.cn',
        [c],
        )
    return 'ok'
# sendmail('1234566')