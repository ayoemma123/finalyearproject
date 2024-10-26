from django.urls import path
from . import views
urlpatterns = [
    path('hf', views.HEARTFAILURE, name = 'hf'),
    path('login', views.login, name = 'login'),
    path('reg', views.register,name = 'reg'),
    path('cad', views.CAD,name= 'cad'),
    path('', views.home,name = ''),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_logout', views.user_logout, name='user_logout'),
]