from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Article
import django.http.request

from .forms import ArticleForm
from django.contrib.auth.decorators import (
    login_required
)

# Create your views here.
def article_view(request, id) -> HttpResponse:
    obj = None
    if id != None:
        obj = Article.objects.get(id=id).content
    return HttpResponse(render_to_string("Articles/article_view.html", context={"content":obj}))

def title_view(request, id) -> HttpResponse:
    obj = None
    if id != None:
        obj = Article.objects.get(id=id).title
    return HttpResponse(render_to_string('Titles/title_view.html', context={"title":obj}))

@login_required
def create_topic_view(request):
    form = ArticleForm(request.POST or None) # take only the first two rows of model form class
    context = {
        "form": form
    }
    if form.is_valid(): # if there's a raising error in the form clean method Flase, else True
        Article_object = form.save()
        context["object"], context["objects"], context["created"] = Article_object, Article.objects.all(), True
    return render(request, "Articles/create.html", context)
# @login_required
# def create_topic_view(request):
#     form = ArticleForm(request.POST or None) 
    
class Search:
    def search_Article_View(self, request) -> HttpResponse:
        obj: None|Article = self.object(self.query(request))
        if obj != None:
            context = self.context(obj)
        return HttpResponse(render_to_string("search_Article/search.html", context=context))
    
    def query(self, request) -> None|int:
        query: django.http.request.QueryDict = request.GET
        try:
            query: int = int(query.get("q"))
        except:
            query: None = None
        return query

    def object(self, query) ->None|Article:
        obj: None = None
        if query != None:
            obj: Article = Article.objects.get(id=query)
        return obj

    def context(self, obj: Article):
        context =  {
            "title":obj.title,
            "content":obj.content
            }
        return context
