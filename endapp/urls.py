from django.urls import path
from endapp import views
app_name='endapp'
urlpatterns = [
    path('login/', views.login,name='login'),
    path('main/', views.main,name='main'),
    path('introduce/', views.introduce,name='introduce'),
    path('menu/', views.menu,name='menu'),
    path('register/', views.register,name='register'),
    path('register1/', views.register1, name='register1'),
    path('mail/', views.mail, name='mail'),
    path('login1/', views.login1, name='login1'),
    path('query1/', views.query1, name='query1'),
    path('query/', views.query, name='query'),
    path('phone/', views.phone, name='phone'),

]