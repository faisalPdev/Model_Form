from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.index,name="home"),
    path('signup/', views.signup,name="signup"),
    path('signin/', views.user_login,name="signin"),
    path('logout/', views.user_logout,name="logout"),
]