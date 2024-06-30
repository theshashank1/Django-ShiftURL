from django.urls import path, include
from . import views

urlpatterns = [
    path('<id>/', views.getURL, name='geturl'),
    path('', views.createShortURL, name='createurl'),
    path('db/<id>', views.getURL_db, name='db'),
    path('db', views.createURL_db, name='createURL_db')
]