from django.urls import path, re_path
from .views import LoginTokenView, UserRegisterView, UsernameCountView, EmailCountView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name='register'),
    re_path("check_email/(?P<email>.*)/count/",
            EmailCountView.as_view(), name='check_email'),
    re_path("check_username/(?P<username>[a-zA-Z0-9]{8,25})/count/",
            UsernameCountView.as_view(), name='check_username'),
    path("login/", LoginTokenView.as_view(), name='token_obtain_pair'),
]
