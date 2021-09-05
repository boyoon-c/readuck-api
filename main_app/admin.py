from django.contrib import admin
from .models import Article, Group, Review, Comment, File

# Register your models here.
admin.site.register(Article)
admin.site.register(Group)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(File)