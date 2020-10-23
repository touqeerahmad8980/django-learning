from django.urls import path
from . import views
from . import followSystemViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    # accounts url
    path('', views.index, name="Login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='login'),
    path('register/', views.userRegister, name="Register"),
    # todo functions page
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('add-item/', views.addItem, name="Add Item"),
    path('remove-item/<int:id>/', views.removeItem, name="Remove"),
    path('edit-item/<int:id>/', views.editItem, name="Edit"),
    # user activities page
    path('activities/', views.activities, name="Activities"),
    path('remove-activity/<int:id>/', views.removeActivities, name="Activities"),
    # follower systems page url
    path('explore/', followSystemViews.exploreUsers, name="Users"),
    path('follow/', followSystemViews.followUsers, name="Follow"),
    path('unfollow/', followSystemViews.unFollowUsers, name="Unfollow"),
    path('followers/', followSystemViews.userFollowers, name="Followers"),
    path('friends/', followSystemViews.userFriends, name="Friends")
]
