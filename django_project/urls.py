"""django_project URL Configuration

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
from main.views import test_view, posts, \
    post_details, hello, sum, pagi, create_car, list_car, create_person, \
    list_person, list_orders, demo, CommentViewSet, \
    AdvViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('comments', CommentViewSet)
r.register('adv', AdvViewSet)
r.register('messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view, name='index'),
    path('posts/', posts, name='post-list'),
    path('posts/<int:post_id>/', post_details, name='post_details'),
    path('hello/', hello, name='hello'),
    path('sum/<a>/<b>/', sum, name='sum'),
    path('pagi/', pagi, name='pagi'),
    path('new_car/', create_car, name='new_car'),
    path('cars/', list_car, name='list_car'),
    path('new_person/', create_person, name='new_person'),
    path('list_person/', list_person, name='list_person'),
    path('orders/', list_orders, name='list_orders'),
    path('demo/', demo),
] + r.urls
