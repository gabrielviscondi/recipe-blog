import random
from django import template

register = template.Library()

@register.simple_tag
def random_class():
   # sclass = ['style1', 'style2', 'style3', 'style4', 'style5', 'style6'] 
   # return random.choice(sclass)
   x = 'style1'
   return (x)