from django.urls import path ,include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('analyse/',views.analyse,name="analyse"),
    
]
