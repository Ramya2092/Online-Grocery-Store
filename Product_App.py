from Categories import *

p = Product()
while True:
    print("\n!! Welcome To Online Store !!")
    print("*** Product Categories *** ")
    print("\n1. Grocery Items")
    C_ID =int(input("\nPlease Enter the Category ID to view Products : "))

    if (C_ID == 1):
        print()
        p.groceries()
        p.buy_product()
    else:
        print("\nPlease Enter Correct Category ID")
        exit()
    
