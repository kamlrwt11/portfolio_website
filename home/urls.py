from django.contrib import admin
from django.urls import path, include
from home import views

# django-admin custmization

admin.site.site_header = "Login To Developer Kamal"
admin.site.site_title = "Welcome To Kamal's Dashboard"
admin.site.index_title = "Welcome To This Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('About',views.About, name='About'),
    path('projects',views.projects, name='projects'),
    path('contact',views.contact, name='contact')
]
