from django import template


register = template.Library()


@register.filter()
def group(lst):
    start = 0
    for i in range(2):
        stop = start + len(lst[i::2])
        yield lst[start:stop]
        start = stop


@register.filter()
def length(lst):
    return len(lst)


@register.filter()
def get_str_by_date(d):
    return d.strftime("%d-%m-%Y")


