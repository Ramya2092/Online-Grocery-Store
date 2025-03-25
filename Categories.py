import itertools 
from collections  import defaultdict

class Product:
        def groceries(self):
                print("     ** Groceries ** ")
                self.Product_Id = [1, 2, 3, 4, 5, 6]
                self.Products = ["Rice", "Dall", "Sugar", "Shampoo", "Face Wash", "Ice Cream"]
                self.Product_Price = [200, 200, 100, 10, 60, 20]
                self.Product_Stock = [20, 5, 10 , 50, 20, 100]
                print("P_Id     ProductName   Price/kg ")
                for (i, j, k) in (zip(self.Product_Id,self.Products,self.Product_Price)):
                        print("{}.        {}        {}".format(i, j, k))
               
        def buy_product(self):
                self.item_id = []
                self.item_purchased =[]
                self.item_quantity= []
                self.item_price = []
                self.item_amount= []
                self.TotalAmount = 0
                self.quantity = 0
                print("\n1 --> Get Product\n2 --> Go to Bill \n3 --> View Stock \n4 --> Reduce Quantity \n5 --> Exit ")
                n = int(input("Enter Your Option : "))
                while n <= 4:   
                        if (n == 1):    
                                p_id = int(input("Enter Product ID :"))
                                if p_id in self.Product_Id:
                                        self.item_id.append(p_id)
                                        quantity = float(input("Enter Quantity : "))
                                        if (self.Product_Stock[p_id- 1] >= quantity ):
                                                print(f"\nItem : {self.Products[p_id -1 ]}\nPrice/KG : {self.Product_Price [p_id - 1]}")
                                                self.item_purchased.append(self.Products[p_id- 1])          
                                                self.item_quantity.append(quantity)
                                                self.item_price.append(self.Product_Price[p_id- 1])
                                                self.item_amount.append(quantity * self.Product_Price[p_id- 1])
                                                print(f"Total Price : {quantity * self.Product_Price[p_id- 1]} ") 
                                                self.TotalAmount +=  quantity * self.Product_Price[p_id- 1]
                                                self.Product_Stock[p_id- 1] = self.Product_Stock[p_id- 1] - quantity
                                        else:  
                                                print("\nOut Of Stock")
                                                print(self.item_id)
                                else:
                                        print("\nInvalid Product ID, Select Correct ID\n") 
                                   
                                print(f"\nTotal Amount :{self.TotalAmount} rs")

                                print("\n1. Next \n2. Go to Bill\n3. View Stocks \n4. Reduce Quantity \n5. Exit ")
                                n = int(input("Enter Your Option: "))

                        if(n == 2):
                                print("\nBilling")
                                print(" P_ID   Product Name   Quantity(in kg)   MRP Price/Kg       Price")
                                try:
                                        merged_data = defaultdict(lambda : [0,0,0,0])
                                        for i in range(len(self.item_id)):
                                                merged_data[self.item_id[i]][0] = self.item_purchased[i]
                                                merged_data[self.item_id[i]][1] += self.item_quantity[i]
                                                merged_data[self.item_id[i]][2] =  self.item_price[i]
                                                merged_data[self.item_id[i]][3] +=  self.item_amount[i]

                                        item_id= list(merged_data.keys())
                                        item_purchased,item_quantity,item_price, item_amount = zip(*merged_data.values())
                                        
                                        self.item_id = list(item_id)
                                        self.item_purchased = list(item_purchased)
                                        self.item_quantity= list(item_quantity)
                                        self.item_price = list(item_price)
                                        self.item_amount = list(item_amount)

                                        for (i, j, q, p, r)  in itertools.zip_longest(item_id,
                                                                                item_purchased,
                                                                                item_quantity,
                                                                                item_price, 
                                                                                item_amount):
                                                                                print(f"{i}     {j}               {q}            {p}            {r} ")

                                                
                                        print("\nTotal Amount ", self.TotalAmount)
                                except:
                                        print("\nKindly Purchase atleat one product, Then only we can print bill")
                                print("\n1. Next \n2. Go to Bill\n3. View Stocks \n4. Reduce Quantity \n5.Exit ")
                                n = int(input("Enter Your Option: "))

                        if(n == 3):
                                print("\nStocks Availabitity")
                                print(" Product Name   Quantity (in kg) ")
                                for (i, q)  in itertools.zip_longest( self.Products,
                                                                        self.Product_Stock,   
                                                                        ):
                                        print(f"  {i}               {q}   ")

                                print("\n1. Next \n2. Go to Bill\n3.View Stocks \n4.Remove products \n5.Exit ")
                                n = int(input("Enter Your Option: "))
                        if (n == 4):                 
                                if len(self.item_id) != 0:              
                                        id = int(input("Enter Product ID :"))
                                        for n in range(len(self.item_id)):
                                                if (self.item_id[n] == id):
                                                        print(f"Total Quantity : {self.item_quantity[n]}")
                                                        Quantity = float(input("Enter Quanity to reduce : "))
                                                        if Quantity <=self.item_quantity[n]:
                                                                self.item_quantity[n] -= Quantity
                                                                print(self.item_quantity[n])
                                                                self.Product_Stock[n] +=  Quantity
                                                                print(self.Product_Stock[n])
                                                                Reduced_Amount = self.Product_Price[id-1] * Quantity
                                                                self.item_amount[n] -= Reduced_Amount
                                                                print("Reduced_Amount", Reduced_Amount)
                                                                self.TotalAmount -= Reduced_Amount
                                                                print("\nTotal Amount : ",self.TotalAmount)

                                                        else:
                                                                print(f"Available Quantity : {self.item_quantity[n]},\nSo, You can't reduce your quantity of the item\n")
                                else:
                                        print("No item listing")        
                                print("\n1. Next \n2. Go to Bill\n3. View Stocks \n4. Reduce Quantity \n5.Exit ")
                                n = int(input("Enter Your Option: "))
                        if (n == 5):
                                print("\nThank You, Well Come Back !!!!")
                                quit()


# o = Product()
# o.groceries()
# o.buy_product()
       
        