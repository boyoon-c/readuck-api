from django.contrib import admin
from .models import Article, Group, Review, Reply, File

# Register your models here.
admin.site.register(Article)
admin.site.register(Group)
admin.site.register(Review)
admin.site.register(Reply)
admin.site.register(File)