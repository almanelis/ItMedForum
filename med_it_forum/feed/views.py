from django.shortcuts import render

def test(request):
    template = 'feed/index.html'
    return render(request, template)