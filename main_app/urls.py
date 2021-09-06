from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/login/', views.Login.as_view(), name='login'),
  path('about/', views.about, name='about'),
  path('signup/', views.signup, name='signup'),
  path('articles/', views.articles_index, name="articles_index"),
  path('articles/<int:article_id>', views.articles_detail, name='articles_detail'),
  path('articles/add/', views.ArticleCreate.as_view(), name='articles_add'),
  path('articles/<int:pk>/update/', views.ArticleUpdate.as_view(), name='articles_update'),
  path('articles/<int:pk>/delete', views.ArticleDelete.as_view(), name='articles_delete'),

  path('articles/<int:article_id>/add_reviews/', views.add_reviews, name='add_reviews'),
  path('articles/<int:review_id>/add_comments/', views.add_replies, name='add_replies'),



  path('groups/', views.GroupList.as_view(), name='groups_index'),
  path('groups/add', views.GroupCreate.as_view(), name='groups_add'),
  path('groups/<int:pk>', views.GroupDetail.as_view(), name='groups_detail'),
  path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='groups_update'),
  path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='groups_delete'),
  # path('login/', views.login, name='login')
]