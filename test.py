# This is the Test file, it provides user interface to the user !
import pickle
import Database.data_server
import Database.design
import Database.functions
import Data_Storage.check_data
def run():
    Database.data_server.display_data()
    Database.design.display_design()
    Database.functions.My_Shopping_Cart()
    f1 = open("Database/total.dat", "rb")
    data = pickle.load(f1)
    total_amount = sum(data)
    if total_amount > 10000:
        Database.design.Bill()
    else:
        Database.design.display_design_cart()
        Data_Storage.check_data.write_data()
run()