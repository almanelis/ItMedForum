from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView


User = get_user_model()

def profile(request):
    return render(request, 'profile/user_profile.html')
    