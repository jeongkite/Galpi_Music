from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path('', views.main, name='main'),
    path('more/', views.more, name='more'),
    path('start/', views.start, name='start'),
    path('question/<int:this_user>/', views.question, name='question'),
    path('end/<int:this_user>/', views.end_story, name='end'),
    path('result/<int:this_user>/', views.calc_result, name='result'),
]
