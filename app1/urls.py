from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('result', views.result),
    path('<url>', views.catch_all)          #This will catch any path not intended to have a page, if you include this it must be the LAST path listed      
]