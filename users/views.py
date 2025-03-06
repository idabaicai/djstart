from django.shortcuts import render, HttpResponse

# Create your views here.


# user/?id=123&name=test
def get_user(request):
    id = request.GET.get('id')
    return HttpResponse(f'<h1>你的 id 是 {id}</h1> name 是 {request.GET.get("name")}')

# user/123/
def get_user_v2(request, id):
    return HttpResponse(f'<h1>你的 id 是 {id}</h1>')