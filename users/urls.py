
from django.urls import path
from . import views

# 命名空间
app_name = 'users'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.get_user, name='user'),
    path('list/<int:id>/', views.get_user_v2, name='user_v2')
]