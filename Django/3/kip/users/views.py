from django.shortcuts import render
from mybackend import functions
import json
from django.contrib.auth.models import User
from django.core import serializers

def profile(request):
    print(request, dir(request))
    username = str(request.user)

    user_dict = functions.get_userinfo(request.user)

    # orders = Orders.objects.filter(owner=user_dict.get('id'))
    # usermessage = UserMessage.objects.filter(user=request.user).order_by('-update_time')
    title = 'Profile : ' + username
    # logging(request, 'access', title)

    return render(request, 'users/profile.html',
                      {'user_list': json.dumps(user_dict), 'title': title})


def users_list(request):
    users = User.objects.all()
    jsonstring_users = serializers.serialize('json', users)
    title = 'User List'
    return render(request, 'users/List.html', {'users_list': jsonstring_users, 'title': title})
