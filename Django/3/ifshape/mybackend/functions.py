from users.models import UserProfile


def get_userinfo(user):
    user_dict = {}
    try:
        c_user = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return user_dict
    except:
        return user_dict

    user_dict['id'] = c_user.id
    user_dict['user_id'] = c_user.user_id
    user_dict['username'] = c_user.username
    user_dict['title'] = c_user.title
    user_dict['group'] = c_user.group
    user_dict['role'] = c_user.role
    user_dict['widgetlist'] = c_user.widgetlist
    user_dict['first_name'] = c_user.user.first_name
    user_dict['last_name'] = c_user.user.last_name
    user_dict['email'] = c_user.user.email
    return user_dict