from django.urls import path
from django.views.generic import TemplateView

app_name = 'test'

urlpatterns = [
    path('', TemplateView.as_view(template_name='test/index.html'))
]
