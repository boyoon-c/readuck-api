from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from .models import Article, Group, Review, Reply
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from main_app import models
import uuid
import boto3
import pandas as pd

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
  reviews = Review.objects.filter(article_id=article_id)
  # Get all replies for reviews that correspond to an article
  reviews_id=[]
  for review in reviews:
    reviews_id.append(review.id)
  replies = Reply.objects.filter(review_id__in=reviews_id)
  review_form = ReviewForm()
  reply_form = ReplyForm()
  return render(request, 'articles/detail.html', 
  { 
    'article': article,
    'reviews': reviews,
    'review_form': review_form,
    'reply_form': reply_form,
    'replies': replies
  })

def add_reviews(request, article_id):
  print("request.user", request.user)
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review=form.save(commit=False)
    new_review.article_id = article_id
    new_review.user = request.user
    new_review.save()
  return redirect('articles_detail', article_id=article_id)

def add_replies(request, article_id, review_id):
  form = ReplyForm(request.POST)
  if form.is_valid():
    new_reply=form.save(commit=False)
    new_reply.review_id=review_id
    new_reply.user = request.user
    new_reply.article_id=article_id
    new_reply.save()
  return redirect('articles_detail', article_id=article_id)

class ReviewUpdate(UpdateView):
  model=Review
  fields = ['content']

class ReviewDelete(DeleteView):
  model=Review
  
  def get_success_url(self):
    print('self', self.object.article_id)
    return reverse('articles_detail', kwargs={'article_id': self.object.article_id })

class ReviewUpdate(UpdateView):
  model=Review
  fields = ['content']

class ReviewDelete(DeleteView):
  model=Review
  
  def get_success_url(self):
    print('self', self.object.article_id)
    return reverse('articles_detail', kwargs={'article_id': self.object.article_id })

class ReplyUpdate(UpdateView):
  model=Reply
  fields = ['content']

class ReplyDelete(DeleteView):
  model=Reply
  
  def get_success_url(self):
    print('self', self.object.review.article_id)
    return reverse('articles_detail', kwargs={'article_id': self.object.review.article_id })




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