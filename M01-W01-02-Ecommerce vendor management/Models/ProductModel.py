class ProductModel:

    def __init__(self):
        self.product_db = dict()

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_db[product_name] = {"product_name": product_name, 
                                         "product_type": product_type, 
                                         "available_quantity": available_quantity, 
                                         "unit_price": unit_price
                                        }
        return True

    def search_product(self, product_name):
        # Search the passed product_name in the dictionary and return the value
        search_product = product.search_product_by_name("Lenovo Gaming")
        if (search_product):
          return (search_product)

    def all_products(self):
        # return all the products available in the dictionary
       all_products = products.get_all_products()
       if (all_products):
           return (all_products)

