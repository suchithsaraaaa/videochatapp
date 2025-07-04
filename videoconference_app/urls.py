from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join_room'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('',views.index, name='index'),
    path('profile/', views.profile, name='profile'),

]
