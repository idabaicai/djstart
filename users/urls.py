
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_user),
    path('list/<int:id>/', views.get_user_v2)
]