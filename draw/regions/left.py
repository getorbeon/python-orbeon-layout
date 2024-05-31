from .left_shipping import shipping

from .financial import financial


def left(image, context):
    context = context['left']
    width = 57

    shipping(image, width, context)
    # obs(image, width, context)
