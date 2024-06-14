

class Basket():
    """"
    A Basket class that provides some methods and properties
    that can be inherited or overrided when necessary.
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number': 1231231}
        self.basket = basket