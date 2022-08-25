from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary 
class Vendor (VendorSessionModel):
 def check_login(self, username):
     if username in VendorSessionModel.vendor_session_db:
         return 'User logged in Successfully'
     def display(self):
         return ("Logged in Successfully")
        else:
            return 'Invalid Username and Password'

    def logout(self, username):
        # Add your code here to log out the current vendor

   if username in VendorSessionModel.vendor_session_db:
       del VendorSessionModel.vendor_session_db[username]
       return 'User Logged out Successfully'

