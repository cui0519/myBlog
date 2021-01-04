from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
=======
# FBV   function based view  基于函数的视图



def index(request):
    return render(request,'index.html')


def detail(request,pk):
    return render(request,'single_article.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')





>>>>>>> f4d958d ('模板复用')
