from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("")

def firstapp(request):
    context = {'tag_var': 'tag_var'}
    return render(request, "index.html", context)