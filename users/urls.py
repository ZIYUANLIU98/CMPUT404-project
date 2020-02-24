from django.urls import path
from . import views

urlpatterns = [
    path('auth_test', views.authenticated_test, name="auth_test"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
]