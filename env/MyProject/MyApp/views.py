from django.shortcuts import render

# Create your views here
def home(requset):
    return render(requset,'home.html')
def menu(requset):
    return render(requset,'menu.html')
def about(requset):
    return render(requset,'about.html')
def contact(requset):
    return render(requset,'contact.html')
def review(requset):
    return render(requset,'review.html')
def category(request):
    return render(request,'category.html')
def learnmore(request):
    return render(request,'learnmore.html')
def veg(request):
    return render(request,'veg.html')
def nonveg(request):
    return render(request,'nonveg.html')