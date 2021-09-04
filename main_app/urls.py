from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.Login.as_view(), name='login'),
  path('about/', views.about, name='about'),
  path('signup/', views.signup, name='signup'),
  path('articles/', views.articles_index, name="articles_index"),
  path('articles/<int:article_id>', views.articles_detail, name='articles_detail'),
  path('articles/add/', views.ArticleCreate.as_view(), name='articles_add'),
  # path('login/', views.login, name='login')
]