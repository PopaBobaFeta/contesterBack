from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
    path('login', views.LoginView.as_view(), name='login'),
    path('test', views.test, name='test'),
    path('logout', views.logout1, name='logout')
]
