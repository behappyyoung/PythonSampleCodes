from django.shortcuts import render
from mybackend import functions
import json


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