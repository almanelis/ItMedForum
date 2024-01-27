from django.db import models
from django.contrib.auth.models import AbstractUser


class Skill(models.Model):
    """Skill model"""
    name = models.CharField('Умения', max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """User model"""
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=14, blank=True, null=True)
    avatar = models.ImageField('Аватар', blank=True, null=True)
    bio = models.TextField('Обо мне', blank=True, null=True)
    github = models.CharField('GitHub', max_length=500, blank=True, null=True)
    skill = models.ManyToManyField(Skill, related_name='users', blank=True)
