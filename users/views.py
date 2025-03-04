from django.shortcuts import render, HttpResponse

# Create your views here.
def get_user(request):
    id = request.GET.get('id')
    return HttpResponse(f'<h1>你的 id 是 {id}</h1>')