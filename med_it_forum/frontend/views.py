from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'frontend/main_page.html'


class ProfilePageView(TemplateView):
    template_name = 'frontend/profile_page.html'


class OtherView(TemplateView):
    template_name = 'frontend/other.html'