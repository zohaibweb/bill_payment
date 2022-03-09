from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.index, name='home'),
    path('newconnection/', views.newuser, name='newcon'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('update/<int:id>/', views.update_data, name='updatedata'),
]