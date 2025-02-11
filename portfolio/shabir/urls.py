from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project',views.project,name='project'),
    path('contact',views.contact,name='contact'),
    path('blog', views.blog, name="blog"),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('resume/',views.download_resume,name='download_resume')

]