from django.forms import ModelForm
from .models import Review, Reply

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['content']

class ReplyForm(ModelForm):
  class Meta: 
    model = Reply
    fields = ['content']