from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="Login"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='login'),
    path('register/', views.userRegister, name="Register"),
    path('add-item/', views.addItem, name="Add Item"),
    path('remove-item/<int:id>/', views.removeItem, name="Remove"),
    path('edit-item/<int:id>/', views.editItem, name="Edit"),
    path('activities/', views.activities, name="Activities"),
    path('remove-activity/<int:id>/', views.removeActivities, name="Activities")
]
