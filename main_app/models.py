from django.db import models
from django.urls import reverse, reverse_lazy
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

# Article
class Article(models.Model):
  author = models.CharField(max_length=250)
  title = models.CharField(max_length=150)
  abstract = models.TextField(
    max_length=500,
    null=True,
    blank=True)
  citation = models.IntegerField()
  journal=models.CharField(max_length=250)
  year= models.IntegerField()
  ## user should be many-to-many
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  ## group should be many-to-many
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('articles_detail', kwargs={'article_id': self.id })
  
  

# Reviews
class Review(models.Model):
  content = models.TextField(
    max_length=500
  )
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse('articles_detail', kwargs={'article_id': self.article_id })
  
  

# Reply
class Reply(models.Model):
  content = models.TextField(
    max_length=500
  )
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)

  def get_absolute_url(self):
    # print(self.review.article_id)
    # print('self', self.review_id)
    return reverse('articles_detail', kwargs={ 'article_id': self.review.article_id})

# Group
class Group(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField(max_length=250)
  # articles = models.ManyToManyField(Article, blank=True)
  participants = models.ManyToManyField(User)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('groups_detail', kwargs={ "pk": self.id })

# Group Articles
class GroupArticle(models.Model):
  author = models.CharField(max_length=250)
  title = models.CharField(max_length=150)
  abstract = models.TextField(
    max_length=500,
    null=True,
    blank=True)
  citation = models.IntegerField()
  journal=models.CharField(max_length=250)
  year= models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  group = models.ForeignKey(Group, on_delete=models.CASCADE)

# def get_absolute_url(self):
#   print('self.id', self.id)
#   return reverse('groups_detail', kwargs={'pk': self.group_id })



class File(models.Model):
  url = models.CharField(max_length=250)
  article = models.OneToOneField(Article, on_delete=models.CASCADE)

'''
# Comment
class Comment(models.Model):
  review=models.ForeignKey(Review,on_Delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# Review
class Review(models.Model):
  article = models.ForeignKey(Article, on_Delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_Delete=models.CASCADE)
  
# Article file
class File(models.Model):
  url=models.CharField(max_length=250)
'''