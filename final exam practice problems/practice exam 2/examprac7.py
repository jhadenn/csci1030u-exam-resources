import unittest

class Product:

    def __init__(self, name, price, weight):

        self.name = name

        self.price = price

        self.weight = weight

    def get_shipping_cost(self):

        return self.weight * 10

    def get_tax(self):

        return self.price * 0.13

    def get_total_price(self):

        return self.price + self.get_shipping_cost() + self.get_tax()
    

class Product_Test(unittest.TestCase) :
    def test_get_shipping_cost(self) :
        item1 = Product('iPhone 15', 999.99, 2)
        self.assertEqual(item1.get_shipping_cost(), 20)

    def test_get_tax(self) :
        item1 = Product('iPhone 15', 999.99, 2)
        self.assertEqual(item1.get_tax(), 129.9987)
    
    def test_get_total_price(self) :
        item1 = Product('iPhone 15', 999.99, 2)
        self.assertEqual(item1.get_total_price(), 1149.9887)

unittest.main()