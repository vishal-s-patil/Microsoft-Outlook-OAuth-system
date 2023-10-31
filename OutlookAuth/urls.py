from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('callback/', views.callback, name='callback'),
    path('signin', views.sign_in, name='signin'),
    path('users', views.get_all_users, name='get_all_users'),
    path('signout', views.signout, name='signout')
]
