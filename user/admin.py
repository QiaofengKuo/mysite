from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


# 拓展用户模型，把nickname添加到用户模型里的写法：
class ProfileInline(admin.StackedInline):
    model = Profile  # 指向Profile模型
    can_delete = False  # 不允许删除


# 继承BaseUserAdmin并添加ProfileInline（自己定义的昵称模型）
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'nickname', 'email', 'is_staff', 'is_active', 'is_superuser')

    # User本身没有nickname字段，故需自定义nickname字段,一个User对应一个Profile,故可以通过user.profile.nickname来得到昵称
    def nickname(self, obj):
        return obj.profile.nickname

    # 把’nickname‘显示为中文
    nickname.short_description = '昵称'


# Re-register UserAdmin
admin.site.unregister(User)  # 取消原先的注册
admin.site.register(User, UserAdmin)  # 再注册添加昵称后的用户模型


# 在后台注册自定义的模型
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')