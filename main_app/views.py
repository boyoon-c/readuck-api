from django.shortcuts import redirect, render
from .models import Article, Group, Review, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app import models
import uuid
import boto3

# Create your views here.
'''
def article_index(request):
  articles = Article.objects.all()
  return render(request, '')
'''
class Login(LoginView):
    template_name='login.html'
    
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up -try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def articles_index(request):
  articles = Article.objects.all()
  return render(request, 'articles/index.html', {'articles': articles})

def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  review = Review.objects.filter(article_id=article_id)
  # comment = Comment.objects.filter()
  return render(request, 'articles/detail.html', 
  { 
    'article':article,
    'review': review 
  })

class ArticleCreate(CreateView):
  model = Article
  fields = '__all__'
  success_url='/articles/'

class ArticleUpdate(UpdateView):
  model = Article
  fields = '__all__'

class ArticleDelete(DeleteView):
  model = Article
  success_url = '/articles/'

class GroupList(ListView):
  model = Group 

class GroupCreate(CreateView):
  model = Group
  fields = '__all__'

class GroupDetail(DetailView):
  model = Group

class GroupUpdate(UpdateView):
  model = Group
  fields = ['articles', 'participants']

class GroupDelete(DeleteView):
  model = Group
  success_url='/groups/'