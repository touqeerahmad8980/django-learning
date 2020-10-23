from django.shortcuts import render,get_object_or_404
from .models import UserContacts
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


def exploreUsers(request):
    users = User.objects.all().exclude(id = request.user.id)
    followers = UserContacts.objects.all()
    return render(request, 'todo-screens/explore.html', {'users':users, 'followers':followers})
    
@csrf_exempt
def followUsers(request):
    following_id = request.GET.get('selected_user_id')
    # check already follow
    try:
        alreadyFollow = UserContacts.objects.get(following_user_id= following_id)
    except UserContacts.DoesNotExist:
        alreadyFollow = None
    # check for friends true
    try:
        bothFollowing = UserContacts.objects.get(user_id=following_id,following_user_id=request.user.id)
    except UserContacts.DoesNotExist:
        bothFollowing = None
        
    if alreadyFollow == None:
        if following_id:
            if bothFollowing == None:
                UserContacts.objects.create(user=request.user,following_user_id=following_id,friends=False)
            else:
                bothFollowing.friends = True
                bothFollowing.save()
                UserContacts.objects.create(user=request.user,following_user_id=following_id,friends=True)
            res = {'code':200, 'following_user_id': following_id}
    else:
        res = {'code':200, 'response':'already follow'}
    return JsonResponse(res)


@csrf_exempt
def unFollowUsers(request):
    following_id = request.GET.get('selected_user_id')
    follower = get_object_or_404(UserContacts, following_user_id= following_id)
    follower.delete()
    # if both follow then
    try:
        unfollowUser = get_object_or_404(UserContacts, user_id=following_id,following_user_id=request.user.id)
    except:
        unfollowUser = None
    if unfollowUser != None:
        unfollowUser.friends = False
        unfollowUser.save()
    # response
    res = {'code':200, 'response': 'Unfollow successfully.'}
    return JsonResponse(res)


def userFollowers(request):
    allFollowers = []
    allFollowings = []
    users = User.objects.all()
    contacts = UserContacts.objects.all()
    for user in users:
        for contact in contacts:
            if contact.user_id == request.user.id:
                if contact.following_user_id == user.id:
                    allFollowings.append(user)
            if contact.following_user_id == request.user.id:
                if contact.user_id == user.id:
                    allFollowers.append(user)
    return render(request, 'todo-screens/followers.html', {'followers':allFollowers, 'followings':allFollowings})


def userFriends(request):
    allFriends = []
    users = User.objects.all()
    contacts = UserContacts.objects.all()
    for user in users:
        for contact in contacts:
            if contact.user_id == request.user.id:
                if contact.friends == True and contact.following_user.id == user.id:
                    allFriends.append(user)
    return render(request, 'todo-screens/friends.html', {'friends':allFriends})
    