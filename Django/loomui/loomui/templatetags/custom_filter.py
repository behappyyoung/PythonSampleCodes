from django import template
from datetime import datetime, timedelta
from django.utils import timezone
from loomui import settings
register = template.Library()


@register.filter
def comma_space(value):
    if value:
        return value.replace(",", ", ")
    else:
        return ''


@register.filter
def my_range(value):
    return xrange(1, value)


@register.filter
def my_range_z(value):
    return xrange(0, value)


@register.filter
def divide(value, arg):
    return value / arg


@register.filter
def list_index(List, i):
    if i >= len(List):
        return []
    else:
        return List[int(i)]


@register.filter
def list_index_add(List, arg):
    i = arg[0] + arg[1]
    if i >= len(List):
        return []
    else:
        return List[int(i)]


@register.simple_tag
def list_index_data(List, i, what):
    if i >= len(List):
        return ''
    else:
        if what == 'asn':
            data = List[int(i)].sample.asn
        else:
            data = getattr(List[int(i)], what)
        return data


@register.simple_tag
def list_find(List, key_value):
    for l in List:
        for k in l.keys():
            if k == key_value:
                return l

    return None

# now = timezone.now()


@register.filter
def is_past_due(value):
    value = value or timezone.now()
    t = value + timedelta(days=10)
    if timezone.now() > t:
        return 'YES'
    else:
        return 'NO'


@register.simple_tag
def tag_git_branch():
    return settings.GIT_BRANCH
