from django.shortcuts import render
from .models import Article

# Create your views here.
'''
def article_index(request):
  articles = Article.objects.all()
  return render(request, '')
'''

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  return render(request, 'signup.html')