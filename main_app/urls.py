from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('',views.Home.as_view(), name = "home"),
    path('noodles/',views.NoodleView.as_view(), name = "noodle_list"),
    path('noodles/new', views.NoodleNew.as_view(), name="noodle_new"),
    path('noodles/<int:pk>/',views.NoodleAbout.as_view(), name='noodle_about')

]