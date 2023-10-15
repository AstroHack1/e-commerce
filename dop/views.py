from django.shortcuts import render

# Create your views here.


def News(request):
    return render(request=request, template_name='news.html') 


def About(request):
    return render(request=request, template_name='about.html') 


def Contact(request):
    return render(request=request, template_name='contact.html') 