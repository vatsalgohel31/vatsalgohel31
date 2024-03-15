# this file is for experiment and use for demo purpose only !
import pickle

import Database.design

file = open("Database/database.dat", "rb")
data = pickle.load(file)
print(data)                             # it will return the dictionary value of data {Product:Rate} form

file2 = open("Database/chocolate_data.dat","rb")
data_2 = pickle.load(file2)
print(data_2)                          # it will return the dictionary value of chocolates data

file3 = open("Database/stationary_data.dat","rb")
data_3 = pickle.load(file3)
print(data_3)                          # it will return the dictionary value of stationary data

file4 = open("Database/chocolates_count.dat","rb")
data_4 = pickle.load(file4)
print(data_4)                         # it will return the list of chocolates product number

file5 = open("Database/stationary_count.dat","rb")
data_5 = pickle.load(file5)
print(data_5)                         # it will return the list of stationary product number

file6 = open("Database/retail.dat","rb")
data_6 = pickle.load(file6)
print(data_6)                        # it will return the retail price of product that your buying

file7 = open("Database/net_quantity.dat","rb")
data_7 = pickle.load(file7)
print(data_7)                        # it will return the net quantity that you are buying

file8 = open("Database/total.dat","rb")
data_8 = pickle.load(file8)
print(data_8)                        # it will return the total bill.

file9 = open("Database/My_Shopping_Cart.dat","rb")
data_9 = pickle.load(file9)
print(data_9)                       # it will return the dictionary value of shopping_cart

file10 = open("Database/Mart_Value.dat","rb")
data_10 = pickle.load(file10)
print(data_10)

file11 = open("Database/Mart_Total.dat","rb")
data_11 = pickle.load(file11)
print(data_11)

file12 = open("Database/Mart_Bill.dat","rb")
data_12 = pickle.load(file12)
print(data_12)

file13 = open("Database/Coupon Code.dat","rb")
data_13 = pickle.load(file13)
print(data_13)

string = "cadbury"
string2 = "five star"
print(string[:3:])
print(string2[:3:])




