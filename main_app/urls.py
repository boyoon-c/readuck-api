from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/login/', views.Login.as_view(), name='login'),
  path('about/', views.about, name='about'),
  path('signup/', views.signup, name='signup'),
  # articles
  path('articles/', views.articles_index, name="articles_index"),
  path('articles/<int:article_id>/', views.articles_detail, name='articles_detail'),
  path('articles/add/', views.ArticleCreate.as_view(), name='articles_add'),
  path('articles/<int:pk>/update/', views.ArticleUpdate.as_view(), name='articles_update'),
  path('articles/<int:pk>/delete', views.ArticleDelete.as_view(), name='articles_delete'),
  # reviews
  path('articles/<int:article_id>/add_reviews/', views.add_reviews, name='add_reviews'),
  path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='update_reviews'),
  path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='delete_reviews'),
  
    # replies
  path('articles/<int:article_id>/<int:review_id>/add_comments/', views.add_replies, name='add_replies'),
  path('replies/<int:pk>/update/', views.ReplyUpdate.as_view(), name='update_replies'),
  path('replies/<int:pk>/delete/', views.ReplyDelete.as_view(), name='delete_replies'),


  # groups
  path('groups/', views.GroupList.as_view(), name='groups_index'),
  path('groups/add', views.GroupCreate.as_view(), name='groups_add'),
  path('groups/<int:pk>', views.GroupDetail.as_view(), name='groups_detail'),
  path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='groups_update'),
  path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='groups_delete'),


  path('groups/<int:pk>/add_articles/', views.GroupArticleCreate.as_view(), name='add_group_articles'),
  path('groups/<int:pk>/delete_articles/', views.GroupArticleDelete.as_view(), name='delete_group_articles'),
  
  # path('login/', views.login, name='login')
]