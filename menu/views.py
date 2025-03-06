from django.shortcuts import render, HttpResponse

# Create your views here.
def get_menu(request, id):
    return HttpResponse(f"你选择的是 {id}")