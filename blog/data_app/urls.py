from django.urls import path
from data_app import views



app_name = 'data_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('post/<int:id>', views.post, name='post'),
    path('service/', views.service, name='service'),
    path('hairdresser/', views.hairdresser, name='hairdresser'),
    path('booking/', views.booking, name='booking'),
    path('contacts/', views.contacts, name='contacts')
]


