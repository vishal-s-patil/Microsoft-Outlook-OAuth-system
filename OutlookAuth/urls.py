from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('v1/callback/', views.callback, name='callback'),
    path('v1/signin', views.sign_in, name='signin'),
    path('v1/users', views.get_all_users, name='get_all_users'),
    path('v1/signout', views.signout, name='signout')
]
