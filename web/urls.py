
from django.contrib import admin
from django.urls import path
from appin5 import views

urlpatterns = [
    path("admin/", admin.site.urls),
     path("",views.index,name="index"),
    path("home1", views.home1, name="home1"),
    path("hai",views.hai,name="hai"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("navigation",views.navigation,name="navigation"),
    path("home",views.home,name="home"),
    path("addData",views.addData,name="addData"),
    path("updateData/<int:id>",views.updateData,name="updateData"),
    path("deleteData/<int:id>",views.deleteData,name="deleteData"),


 
]
