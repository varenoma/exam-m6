from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpView, HomePage, logout_def

app_name = 'accaunt'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='accaunt/signin.html'),
         name='signin'),
    path('logout/', logout_def, name='logout'),
]
