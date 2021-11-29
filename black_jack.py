import random
print(" Game is Start")
player_sum = 0 
dealer_sum = 0
player = 0
dealer = 0
for i in range(1,4):
    if i == 1:

        for j in range(i):

            player = random.randint(2,11)
            print("player number is:\n",player)
            player_sum = player_sum + player
            print("score of player is:\n",player_sum)
            print("*******************************")
            dealer = random.randint(2,11)
            print("dealer number is:\n",dealer)
            dealer_sum = dealer_sum + dealer
            print("score of dealer is:\n",dealer_sum)
            print("*******************************")
            input("Press Enter \n")
            print("*******************************")
           
           
           
            
            

    if i == 2:
        
        player = random.randint(2,11)
        print("player number is:\n",player)
        player_sum = player_sum + player
        print("score of player is:\n",player_sum)
        print("*******************************")
        if player_sum == 21:
            print("***player Got Blackjack!***")
            break
        if player_sum > 21:
            print("Dealer Win!")
            break
        
        dealer = random.randint(2,11)
        print("dealer number is:\n Hidden")
        dealer_sum = dealer_sum + dealer
        print("score of dealer is:\n Hidden\n")
        print("Player choose the option \n")
      

    
        while player_sum < 21:

            option = input("enter H to Hit and enter S to Stand:-").lower()
            if option == 'h':
                player = random.randint(2,11)
                print("player number is:\n",player)
                player_sum = player_sum + player
                print("score of player is:\n",player_sum)
                if player_sum > 21:
                    print("Dealer Win!")
                    print("*******************************")
                    continue
                if player_sum == 21:
                    print("***player Got Blackjack!***")
                
                print("dealer's 2'nd card score is :",dealer)
                print("\n score of dealer is:\n",dealer_sum)
                print("*******************************")
                    
                if player_sum <  dealer_sum :
                        print("Dealer Win!") 
                        break
                
                dealer = random.randint(2,11)
                print("dealer number is:\n",dealer)
                dealer_sum = dealer_sum + dealer
                print("score of dealer is:\n",dealer_sum)

                if dealer_sum == player_sum:
                    print("Match Tie! \n Game Over! ")
                if dealer_sum == 21:
                    print("***Dealer Got Blackjack!***")
                    break
                if dealer_sum > 21:
                    print("Player Win!")
                    break
                if dealer_sum > player_sum:
                    print("Dealer Win!")
                    break
                else :
                    print("Player Win!") 
                    break   
            

            if option == 's':
                print("score of player is:\n",player_sum)
                print("dealer's 2'nd card score is :",dealer)
                print("\n score of dealer is:\n",dealer_sum)
                if dealer_sum == 21:
                    print("***Dealer Got Blackjack***")
                    break
                if dealer_sum > 21 :
                    print("player Win") 
                    break
                if dealer_sum > player_sum:
                    print("Dealer Win!")
                    break
                
                dealer = random.randint(2,11)
                print("dealer number is:\n",dealer)
                dealer_sum = dealer_sum + dealer
                print("score of dealer is:\n",dealer_sum)
                if dealer_sum == player_sum:
                    print("Match Tie! \n Game Over! ")
                    break
                if dealer_sum < player_sum :
                    print("Player Win!")
                    break
                if dealer_sum > player_sum:

                    print("Dealer Win!") 
                    break  
                if dealer_sum > 21:
                    print("Player Win!") 

            else:
                print("Please press only H or S")
                        
               
            
                
                
                


                    
        
        
       
    






