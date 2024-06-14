

class Basket():
    """"
    A Basket class that provides some methods and properties
    that can be inherited or overrided when necessary.
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product):
        '''
        adding and updating the basket
        '''
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price':str(product.price)}
        
        self.session.modified = True
