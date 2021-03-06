from django.forms import ModelForm
from .models import Article

class PostForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'cover', 'body']