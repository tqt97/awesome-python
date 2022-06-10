from decimal import Decimal

from store.models import Product


class Basket():
    '''
    A base Basket class, providing some default behaviors that can be inherited or override, as necessary.
    '''

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def __iter__(self):
        '''
        Collect the product_id in the session data to query the database and
        return product objects
        '''
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        '''
        Get the basket data and count the qty items
        '''
        return sum(item['qty'] for item in self.basket.values())

    def add(self, product, qty):
        '''
        Adding a product to the basket session data
        '''
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def delete(self, product):
        '''
        Delete item from session data
        '''
        product_id = str(product)
        # print(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def save(self):
        '''
        Save the basket session data
        '''
        self.session.modified = True
