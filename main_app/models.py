from django.db import models
from django.urls import reverse
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
    return reverse('articles_detail', kwargs={'article_id', self.id })

'''
# Group
class Group(models.Model):
  ## article many-to-many
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ## user many-to-many
  user = models.ForeignKey(User, on_delete=models.CASCADE)

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