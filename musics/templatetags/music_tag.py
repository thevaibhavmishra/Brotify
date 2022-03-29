from atexit import register
from unicodedata import name
from django import template
import math

register = template.Library()

@register.filter(name= 'time_formatter')
def time_formatter(time):
    time = int(time)
    min = math.floor((time%3600/60))
    sec = math.floor(time%60)
    if sec<10 :
        sec = f"0{sec}"
    return f"{min}:{sec}"
