from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:id>', views.get_menu)
]