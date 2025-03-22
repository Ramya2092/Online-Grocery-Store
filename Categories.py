import itertools 
class Product:
        def groceries(self):
                print("     ** Groceries ** ")
                self.Product_Id = [1, 2, 3]
                self.Products = ["Rice", "Dall", "Sugar"]
                self.Product_Price = [200, 200, 100]
                self.Product_Stock = [20, 5, 10 ]
                print("P_Id     ProductName   Price ")
                for (i, j, k) in (zip(self.Product_Id,self.Products,self.Product_Price)):
                        print("{}.        {}        {}".format(i, j, k))
               
        def buy_product(self):
                self.item_purchased =[]
                self.item_quantity= []
                self.item_price = []
                self.item_amount= []
                self.TotalAmount = 0
                self.quantity = 0
                print("\n1 --> Get Product\n2 --> Go to Bill \n3 --> View Stock \n ")
                n = int(input("Enter Your Option : "))
                while n <= 3:   
                        if (n == 1):    
                                p_id = int(input("Enter Product ID :"))
                                if (p_id == 1):
                                        quantity = float(input("Enter Quantity : "))
                                        if (self.Product_Stock[0] < quantity ):
                                                print("\nOut Of Stock")
                                        else:
                                                print("\nItem : Rice\nPrice/KG : 200")
                                                self.item_purchased.append(self.Products[0])          
                                                self.item_quantity.append(quantity)
                                                self.item_price.append(self.Product_Price[0])
                                                self.item_amount.append(quantity * self.Product_Price[0])
                                                self.TotalAmount +=  quantity * self.Product_Price[0]
                                                self.Product_Stock[0] = self.Product_Stock[0] - quantity
                                elif (p_id == 2):
                                        quantity = float(input("Enter Quantity : "))
                                        if (self.Product_Stock[1] < quantity ):
                                                print("\nOut Of Stock")
                                        else:
                                                print("\nItem : Dall\nMRP Price/KG : 200")
                                                self.item_purchased.append(self.Products[1])      
                                                self.item_quantity.append(quantity)
                                                self.item_price.append(self.Product_Price[1])
                                                self.item_amount.append(quantity * self.Product_Price[1])
                                                self.TotalAmount +=  quantity * self.Product_Price[1]
                                                self.Product_Stock[1] = self.Product_Stock[1] - quantity
                                elif (p_id == 3):
                                        quantity = float(input("Enter Quantity : "))
                                        if (self.Product_Stock[2] < quantity ):
                                                print("\nOut Of Stock")
                                        else:
                                                print("\nItem : Sugar\nPrice/KG : 100")
                                                self.item_purchased.append(self.Products[2])            
                                                self.item_quantity.append(quantity)
                                                self.item_price.append(self.Product_Price[2])
                                                self.item_amount.append(quantity * self.Product_Price[2])
                                                self.TotalAmount +=  quantity * self.Product_Price[2]
                                                self.Product_Stock[2] = self.Product_Stock[2] - quantity                
                                else:
                                        print("\nInvalid Product ID, Select Correct ID\n")     
                                print(f"\nTotal Amount :{self.TotalAmount} rs")

                                print("\n1. Next \n2. Go to Bill\n3.View Stocks \n4.Exit ")
                                n = int(input("Enter Your Option: "))

                        if(n == 2):
                                print("\nBilling")
                                print(" Product Name   Quantity  MRP Price/Kg       Price")
                                for (i, q, p, a)  in itertools.zip_longest(self.item_purchased,
                                                                           self.item_quantity,
                                                                           self.item_price,
                                                                           self.item_amount
                                                                           ):
                                        print(f"  {i}            {q}         {p}             {a}")
                                print("\nTotal Amount ", self.TotalAmount)
                        
                                print("\n1. Next \n2. Go to Bill\n3.View Stocks \n4.Exit ")
                                n = int(input("Enter Your Option: "))

                        if(n == 3):
                                print("\nStocks Availabitity")
                                print(" Product Name   Quantity ")
                                for (i, q)  in itertools.zip_longest( self.Products,
                                                                        self.Product_Stock,   
                                                                        ):
                                        print(f"  {i}            {q}   ")

                                print("\n1. Next \n2. Go to Bill\n3.View Stocks \n4.Exit ")
                                n = int(input("Enter Your Option: "))

                        if (n == 4):
                                print("\nThank You, Well Come Back !!!!")
                                quit()



       
        