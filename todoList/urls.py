from django.urls import path
from todoList.views import index,dashboard,userRegister,addItem,removeItem,editItem
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="Login"),
    path('dashboard/', dashboard, name="Dashboard"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='login'),
    path('register/', userRegister, name="Register"),
    path('add-item/', addItem, name="Add Item"),
    path('remove-item/<int:id>/', removeItem, name="Remove"),
    path('edit-item/<int:id>/', editItem, name="Edit")
]
