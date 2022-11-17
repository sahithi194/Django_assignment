from .import views
from django.urls import path

urlpatterns =[
    path('Homepage/',views.HomePage),
    path('Indexpage/',views.IndexPage),
] 