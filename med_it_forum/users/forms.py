from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView

from users.models import Skill

# Получаем модель пользователя:
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # Наследуем класс Meta от соответствующего класса родительской формы.
    # Так этот класс будет не перезаписан, а расширен.
    class Meta(UserCreationForm.Meta):
        model = User
        ## атрибут fields — список полей, которые будут выведены в HTML-форму.
        fields = ('username', 'email',)


class CustomUserUpdateForm(UserChangeForm):
    """Форма редактирования профиля пользователя"""
    skill = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Навыки',
        )
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'phone', 'bio', 'github', 'avatar', 'skill')