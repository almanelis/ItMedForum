from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from froala_editor.fields import FroalaField

from users.models import Skill

User = get_user_model()

class Post(models.Model):
    """Модель поста"""

    title = models.CharField('Заголовок', max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # content = models.TextField('Контент')
    content = FroalaField()
    picture = models.ImageField('Картинка', upload_to='post_images',blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    tags = models.ManyToManyField(Skill, verbose_name="Теги")

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse("feed:detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.title
    