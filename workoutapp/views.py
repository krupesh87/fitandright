from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coach(request):
    return render(request, 'coach.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')


def success_story(request):
    return render(request, 'success_story.html')


def blog(request):
    return render(request, 'blog.html')



    
    