import random
print(" Game is Start")
player_sum = 0 
dealer_sum = 0
player = 0
dealer = 0
player = random.randint(2,11)
print("player number is",player)
player_sum = player_sum + player
print("score of player is",player_sum)
dealer = random.randint(2,11)
print("dealer number is",dealer)
dealer_sum = dealer_sum + dealer
print("score of dealer is",dealer_sum)



