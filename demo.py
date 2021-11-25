def vendingmachine(): 
    a = {'item_name':'coke','price': 25}
    b = {'item_name':'pepsi','price': 35}
    c = {'item_name':'soda','price': 45}
    items = [a,b,c]
    c1 = {'coin':'penny','coin_value': 1}
    c2 = {'coin':'nickle','coin_value': 5}
    c3 = {'coin':'dime','coin_value': 10}
    c4 = {'coin':'quarter','coin_value': 25}
    coin = [c1,c2,c3,c4]
   
    print("Welcome to Vending machine")
    print("Available Items Are :")
    for i  in items:
        print(i) 
   
    def selection():
        price = int(input("press 25 for coke \n press  35 for pepsi \n  press 45 for soda : "))
        if price == 25:
            print("Your Choice is coke and their price is 25 \n Accepted Coins Are: 1,5,10,25")
            price = 1
            amt= 0
            while price <= 25:
                coins = int(input("Enter coins  i.e 1 , 5 , 10 ,25"))

                if coins==1 or coins==5 or coins==10 or coins==25:
                    value1=int(input("how many coins you are insert..."))
                    amt=amt+(coins*value1)
                    if amt < 25:
                        print("remaining coins is",25-amt,"please insert")
                    if amt>=25:
                        print("your order is ready \n Remaining amt is ",amt-25)
                        print("******Thank you! Have a Nice Day!*******")
                        break
                else:
                    print("Please Insert valid Coins i.e: 1,5,10,25")
                price = +1
        if price == 35:
            print("Your Choice is pepsi and their price is 35 \n Accepted Coins Are: 1,5,10,25")
            price = 1
            amt = 0
            while price <= 35:
                coins = int(input("Enter coins  i.e 1 , 5 , 10 ,25"))

                if coins == 1 or coins == 5 or coins == 10 or coins == 25:
                    value = int(input("how many coins you are insert..."))
                    amt = amt+(coins*value)
                    if amt < 35:
                        print("remaining coins is",35-amt,"please insert")
                    if amt >= 35:
                        print("your order is ready \n Remaining amt is ",amt-35)
                        print("******Thank you! Have a Nice Day!*******")
                        break
                else:
                    print("Please Insert valid Coins i.e: 1,5,10,25")
                price = +1

        if price == 45:
            print("Your Choice is soda and their price is 45 \n Accepted Coins Are: 1,5,10,25")
            price=1
            amt=0
            while price <= 45:
                coins = int(input("Enter coins  i.e 1 , 5 , 10 ,25"))

                if coins == 1 or coins == 5 or coins == 10 or coins == 25:
                    value_3=int(input("how many coins you are insert..."))
                    amt = amt + (coins * value_3)
                    if amt < 45:
                        print("remaining coins is",45-amt,"please insert")
                    if amt >= 45:
                        print("your order is ready \n Remaining amt is ",amt-45)
                        print("******Thank you! Have a Nice Day!*******")
                        break
                else:
                    print("Please Insert valid Coins i.e: 1,5,10,25")
                price = +1
    selection()    
vendingmachine()    


            
                
                    

                        

            


        
        
          
        
        
                
          


                

 

            
    
        
            

        
          
              
           
        


        
    
    


       
    
   


      