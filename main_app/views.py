from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
# from .models import Article, Group, GroupArticle, Review, Reply, File
from .models import *
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

S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/'
BUCKET = 'my-readuck-bucket'

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

@login_required
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

class ReviewUpdate(LoginRequiredMixin, UpdateView):
  model=Review
  fields = ['content']

class ReviewDelete(DeleteView):
  model=Review
  
  def get_success_url(self):
    print('self', self.object.article_id)
    return reverse('articles_detail', kwargs={'article_id': self.object.article_id })

class ReplyUpdate(LoginRequiredMixin, UpdateView):
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

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the groups
    context['group_article_list'] = GroupArticle.objects.filter(group_id=self.object.id)
    print('context', context['group_article_list'])
    return context

class GroupUpdate(UpdateView):
  model = Group
  fields = ['name','description', 'participants']

class GroupDelete(DeleteView):
  model = Group
  success_url='/groups/'

class GroupArticleCreate(CreateView):
  model = GroupArticle
  fields=['author', 'title', 'abstract', 'citation', 'journal', 'year']

  def get_success_url(self):
    print('self', self.object.group_id)
    return reverse('groups_detail', kwargs={'pk': self.object.group_id })

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.group_id = self.kwargs['pk']
    print('kwargs', self.kwargs['pk'])
    response=super().form_valid(form)
    return response


class GroupArticleUpdate(UpdateView):
  model = GroupArticle
  fields=['']

class GroupArticleDelete(DeleteView):
  model = GroupArticle

  def get_success_url(self):
    return reverse('groups_detail', kwargs={'pk': self.object.group_id })

def add_file(request, article_id):
  article_file = request.FILES.get('article-file', None)
  if article_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + article_file.name[article_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(article_file, BUCKET, key)
      url = f'{S3_BASE_URL}{BUCKET}/{key}'
      article = File(url=url, article_id=article_id)
      article_file = File.objects.filter(article_id=article_id)
      if article_file.first():
        article_file.first().delete()
      article.save()
    except Exception as err:
      print('An error occured uploading file to S3: %s' % err)
  return redirect('articles_detail', article_id=article_id)


def profile(request):
  articles = Article.objects.filter(user=request.user)
  reviews = Review.objects.filter(user=request.user)
  replies = Reply.objects.filter(user=request.user)
  groups=Group.objects.all()
  user_group=[]
  for g in groups:
    for p in g.participants.all():
      if p==request.user:
        user_group.append(g)

  return render(request, 'profile.html', {
    'articles': articles,
    'reviews': reviews,
    'replies': replies,
    'user_group': user_group
  })

def search(request):
  if request.method =='GET':
    article_title=request.GET.get('query')
    try: 
      status=Article.objects.filter(title__icontains=article_title)
      return render(request, 'search.html', {"articles": status })
    except:
      return render(request, "search.html", {"articles": status})
  else:
    return render(request, "search.html", {})