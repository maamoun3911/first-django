from django.http import HttpResponse
from django.template.loader import render_to_string
from secapp.models import Article

def home_view(request):
    all_objects = Article.objects.all()
    
    context: dict = {
        "all_objects": all_objects,
    }
    response = render_to_string('home.html', context=context)
    return HttpResponse(response)