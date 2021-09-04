from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.Login.as_view(), name='login'),
  path('about/', views.about, name='about'),
  path('signup/', views.signup, name='signup'),
  # path('login/', views.login, name='login')
]