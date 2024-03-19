from django.urls import path
from django.contrib.auth.views import LoginView, SignupView, LogoutView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('logout/', LogoutView.as_view, name='account_logout'),
]