from .left_shipping import shipping
from .left_obs import obs
from .left_financial import financial


def left(image, context):
    context = context['left']
    width = 57
    financial(image, width, context)
    shipping(image, width, context)
    obs(image, width, context)
