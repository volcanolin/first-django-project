"""为应用程序users定义URL模式"""

from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# 修改模板路径
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登录界面
    path('login/', LoginView.as_view(), name='login'),
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),
    # path(r'^logout/$', LogoutView.as_view(), name='logout'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]
app_name = 'users'
