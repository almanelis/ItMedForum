from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from feed.models import Post


User = get_user_model()

def profile(request):
    user = request.user 
    user_posts = Post.objects.filter(author=user)
    context = {
        'user_posts': user_posts,
    }
    template = 'profile/user_profile.html'
    
    return render(request, template, context)
    
