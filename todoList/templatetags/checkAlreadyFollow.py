from todoList.models import UserContacts
from django import template
register = template.Library()

@register.filter(name='checkAlreadyFollow')
def checkAlreadyFollow(request,id):
    try:
        alreadyFollow = UserContacts.objects.get(user_id=request.user.id, following_user_id=id)
    except UserContacts.DoesNotExist:
        alreadyFollow = 0
    return alreadyFollow