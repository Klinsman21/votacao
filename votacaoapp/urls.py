"""votacao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.generic import TemplateView
from votacaoapp import views

app_name = 'votacaoapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create-voting/', views.CreateVoting.as_view(), name='voting-create'),
    path('list/', views.VotingList.as_view(), name='voting-list'),
    path('list1/<pk>', views.VotingTrue.as_view(), name='voting-true'),
    path('list2/<pk>', views.VotingFalse.as_view(), name='voting-false'),
    path('popup', views.Popup.as_view(), name='popup'),
    path('comments/<pk>', views.Comments.as_view(), name='comments'),
    path('comments2/<pk>', views.CommentsView.as_view(), name='commentsview'),
]
