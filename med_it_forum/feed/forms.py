from django import forms

from users.models import Skill
from .models import Post


class PostForm(forms.ModelForm):
    """Форма создания поста на основе модели поста"""
    tags = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Теги',
        )

    class Meta:
        model = Post
        exclude = ('author',)
