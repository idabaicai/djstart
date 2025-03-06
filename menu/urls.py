from django.urls import path
from . import views

# 命名空间
app_name = 'menu'

urlpatterns = [
    path('list/<int:id>', views.get_menu, name='list')
]