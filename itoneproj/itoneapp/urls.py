from django.urls import path
from . import views

app_name = 'itoneapp'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login_page, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('journal_entry/', views.journal_entry, name='journal_entry'),

]
