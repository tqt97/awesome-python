from .basket import Basket


def basket(request):
    return {'basket': Basket(request)}  # <-- this is the key to the context processor
