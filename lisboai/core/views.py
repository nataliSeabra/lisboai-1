from django.shortcuts import render
from lisboai.core.models import Article

# Create your views here.

def home(request,template_name="index.html"):

    obj = Article.objects.all()
    
    return render(request,template_name,{"data":obj})
    
    

def about(request,template_name="about.html"):

    return render(request,template_name)

