from django.urls import include, path

from .import views

urlpatterns = [
    path('scrapy/', views.scrapy,name='scrapy'),
    path('/', views.scrapy,name='scrapy1')

]
