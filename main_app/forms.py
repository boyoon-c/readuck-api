from django.forms import ModelForm
from .models import GroupArticleReview, Review, Reply

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['content']

class ReplyForm(ModelForm):
  class Meta: 
    model = Reply
    fields = ['content']

class GroupArticleReviewForm(ModelForm):
  class Meta:
    model=GroupArticleReview
    fields=['content']