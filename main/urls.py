from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('browsebook/', views.browsebook, name='browsebook'),
    path('addbook/', views.addbook, name='addbook'),
    path('mylisting/', views.mylisting, name='mylisting'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('passwordreset/', views.passwordreset, name='passwordreset'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('manage_contacter/', views.manage_contacter, name='manage_contacter'),
    path('FAQ_S/', views.FAQ_view, name='FAQ_S'),
    
   
    
]

