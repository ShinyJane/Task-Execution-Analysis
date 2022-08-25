from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel
from VendorImplementation import VendorImplementation


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price, login_res=None):
        # check if the vendor is logged in, then add the product and return True else Return False

      class ProductsImplementation (VendorImplementation)
          vendor = VendorImplementation()

            login_res = vendor.login('Gosling, gosling_pw'):
            if login_res == False
                print ("Invalid Username and Password")
            else:
                 product = ProductsImplementation()
                product.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
                product.add_product("Lenovo Gaming", "Laptop", 40, 20000)


     def search_product_by_name(self, product_name):
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        search_product = products.search_product_by_name("Lenovo Gaming")
        if (search_product):
            return (search_product)
        else:
            return ("False")

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products

        all_products = products.get_all_products()
        if (all_products):
            return(all_products)
        else:
            return(False)


