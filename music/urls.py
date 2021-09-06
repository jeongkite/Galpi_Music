from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path('', views.main, name='main'),
    path('more/', views.more, name='more'),
    path('start/', views.start, name='start'),
    path('question/<str:code>/', views.question, name='question'),
    path('end/<str:code>/', views.end_story, name='end'),
    path('result/<str:code>/', views.calc_result, name='result'),
]
