"""secproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from secproject import views
from secapp.views import (
    Search, create_topic_view, title_view, article_view
)
from accounts.views import (
    login_view, logout_view, sign_up_view
    )

urlpatterns = [
    path('', views.home_view),
    path("accounts/logout/", logout_view),
    path("accounts/login/", login_view),
    path("accounts/register/", sign_up_view),
    path('Articles/create/', create_topic_view),
    path('Articles/<int:id>/', article_view),
    path('search_Article/', Search().search_Article_View),
    path('Titles/<int:id>/', title_view),
    path('admin/', admin.site.urls),
]