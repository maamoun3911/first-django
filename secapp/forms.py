from django import forms
from .models import Article

# the form it self is a model class or can be a model class
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ["title", "content"]
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title, content = cleaned_data.get("title"), cleaned_data.get("content")
        qst = Article.objects.filter(title__icontains=title)
        qsc = Article.objects.filter(content__icontains=content)
        if qst.exists():
            self.add_error("title", "repeated title")
        if qsc.exists():
            self.add_error("content", "repeated content")
        if qst.exists() and qsc.exists():
            raise forms.ValidationError("both repeated %(tit)s & %(con)s"
                , params={
                    "con": "content", 
                    "tit": "title"
                    }
                )
        return cleaned_data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    def find_repeat_content(self) -> list[Article.title, Article.content]:
        all_objects: Article = Article.objects.all()
        return [obj.title for obj in all_objects], [obj.content for obj in all_objects]

    def clean(self):
        cleaned_data = self.cleaned_data
        title, content = cleaned_data.get("title"), cleaned_data.get("content")
        repeated_title, repeated_content = self.find_repeat_content()
        if title in repeated_title:
            self.add_error("title", "repeated title <title error>")
        if content in repeated_content:
            self.add_error("content", "repeated content <content error>")
        if title in repeated_title and content in repeated_content:
            raise forms.ValidationError(
                f'repeated {title} & {content}',
                params={
                    'title':"title",
                    "content":"content"
                    }
            )
        return cleaned_data # not necesseray