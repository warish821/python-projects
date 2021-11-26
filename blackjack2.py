import random
import os
import time
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
s = ' '
for card in cards:
    if card == 'A':
        for i in card:
            print("\t---------------------\n\t    {}       ".format(card),"    {}".format(suits_values['Spades']))
        for i in range(13):
            print("\t|",end="")
            print("                   |")
            if i>11:
                print("\t   {}       ".format(suits_values['Spades']),"    {}".format(card))
                print("\t---------------------")
                
for card in cards:
    if card == 'A':
        for i in card:
            print("\t---------------------\n\t    {}       ".format(card),"    {}".format(suits_values['Hearts']))
        for i in range(13):
            print("\t|",end="")
            print("                   |")
            if i>11:
                print("\t   {}       ".format(suits_values['Hearts']),"    {}".format(card))
                print("\t---------------------")
for card in cards:
    if card == 'A':
        for i in card:
            print("\t---------------------\n\t    {}       ".format(card),"    {}".format(suits_values['Clubs']))
        for i in range(13):
            print("\t|",end="")
            print("                   |")
            if i>11:
                print("\t   {}       ".format(suits_values['Clubs']),"    {}".format(card))
                print("\t---------------------") 
for card in cards:
    if card == 'A':
        for i in card:
            print("\t---------------------\n\t    {}       ".format(card),"    {}".format(suits_values['Diamonds']))
        for i in range(13):
            print("\t|",end="")
            print("                   |")
            if i>11:
                print("\t   {}       ".format(suits_values['Diamonds']),"    {}".format(card))
                print("\t---------------------")  
                              
                               
                
                    
            
                
              
              
             
            
              
            
            
        