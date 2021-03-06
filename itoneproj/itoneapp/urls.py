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
    path('savejournal/', views.savejournal, name='savejournal'),
    path('journal_list/', views.journal_list, name='journal_list'),
    path('delete_journal/<int:journal_detail_id>', views.delete_journal, name='delete_journal'),
    path('edit_journal/<int:journal_detail_id>', views.edit_journal, name='edit_journal'),
    path('edit_save/<int:journal_detail_id>', views.edit_save, name='edit_save'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('profile_edit/<int:user_id>/', views.profile_edit, name='profile_edit'),
    path('profile_edit_save/<int:user_id>/', views.profile_edit_save, name='profile_edit_save'),









]
