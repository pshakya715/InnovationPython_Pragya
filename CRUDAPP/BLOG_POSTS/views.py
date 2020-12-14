from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome to this website.")


def deleteapp(request):
    context = {'tag_vars': "tag_vars"}
    return render(request, 'BLOG_POSTS/POST_DELETE.html', context)


def formapp(request):
    context = {'tag_vars1': "tag_vars1"}
    return render(request, 'BLOG_POSTS/POST_FORM.html', context)


def listapp(request):
    context = {'tag_vars2': "tag_vars2"}
    return render(request, 'BLOG_POSTS/POST_LIST.html', context)

