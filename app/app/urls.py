"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from todo import views
import ftd_django

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/get-data", views.get_data),
    path("api/post-data", views.post_data),
    path("api/update-status", views.update_todo),
    path("api/add-task", views.add_task),
    path("api/reset-todo", views.reset_todo),
    path("api/delete-task", views.delete_todo),
    path("api/sort-todo", views.sort_todo),
    path("", views.IndexView.as_view()),
] + ftd_django.static()
