from django.urls import path

from .views import SignUpView, HomePage, logout_def

app_name = 'accaunt'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_def, name='logout')
]
