from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login.index'),
    path('login/', views.login_view, name='login.login_view'),
    path('login_auth/', views.login_auth, name='login.login_auth'),
    path('logout/', views.logout_view, name='login.logout_view'),
    path('register/', views.register_view, name="login.register_view"),
]
