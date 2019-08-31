from django.db import models 
from django.contrib.auth.models import User

""" 自定义用户模型
1、继承Django的用户模型
2、新的模型拓展关联User
方法二比较简单，此处使用方法二，详细可到官方文档查看实例"""


# 创建自定义昵称模型
class Profile(models.Model):
    # 使用一对一外键关联User， 一个用户对应一个昵称
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name='昵称')

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nickname, self.user.username)


# User模型动态绑定Profile模型里的nickname
def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ' '


def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username


def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


# User里创建get_nickname属性
User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname
