from django.urls import path

from .views import ListViewQatagon, DetailViewQatagon, UpdateViewQatagon, DeleteViewQatagon, search_view

app_name = 'qatagon'

urlpatterns = [
    path('', ListViewQatagon.as_view(), name='home'),
    path('detail/<int:pk>', DetailViewQatagon.as_view(), name='detail'),
    path('detail/<int:pk>/update', UpdateViewQatagon.as_view(), name='update'),
    path('detail/<int:pk>/delete', DeleteViewQatagon.as_view(), name='delete'),
    path('search/', search_view, name='search'),

]
