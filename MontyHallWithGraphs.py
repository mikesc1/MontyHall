# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:34:33 2020

@author: micha
"""

              
def game():
    picked_set = [1,2,3]
    possible_pick = [1,2,3]
    spare_door = [1,2,3]
    
    
    prize_location = np.random.randint(1,4)
    
    possible_pick.remove(prize_location)
    
    spare_door.remove(prize_location)
    
    bet = int(input('Place your bet: $'))
    
    first_door_choice = int(input('Choose door: 1, 2, or 3:   '))
    
    print('You picked door ' + str(first_door_choice)+ '\n')
    
    picked_set.remove(first_door_choice)
    if first_door_choice == prize_location:
        random_item_from_list = random.choice(spare_door)
        spare_door.remove(random_item_from_list)
        print("host opens door number [" + str(random_item_from_list) + "] and there is nothing behind it\n")
        print('Would you rather keep door number [' + str(first_door_choice) + '] or pick door number ' + str(spare_door) + '?')
        final_choice1 = int(input('Final Choice: '))
        if final_choice1 == prize_location:
            print('You win!')
            cash.append(sum(cash)+bet)
    
        else:
            print('You lose')
            cash.append(sum(cash)-bet)
    
        
    
    else:
        spare_door.remove(first_door_choice)
        print("host opens door number" + str(spare_door) + " and there is nothing behind it\n")
        print('Would you rather keep door number [' + str(first_door_choice) + '] or pick door number [' + str(prize_location) + '] ?')
        final_choice = int(input('Final Choice: '))
        if final_choice == prize_location:
            print('You win!')
            cash.append(sum(cash)+bet)
            
        else:
            print('You lose')
            cash.append(sum(cash)-bet)

while True:
    import numpy as np
    import random
    import matplotlib.pyplot as plt

    cash = []
    switch_win = []
    switch_loose = []
    keep_win = []
    keep_loose = []
            
    name = input('Who is playing?\n')    
    rounds = int(input('How many rounds would you like to play?'))
               
    for i in range(rounds):
        game()
    if sum(cash) < 0:
        print('\nGame Over\nYou lost money')
    else:
        print('\nGame Over\nYou won money')
        
    print('Final earnings $' + str(sum(cash)) + '\n')
    plt.plot(np.arange(1,rounds+1,1),cash,'-', label = 'so sad', linewidth = 5, color = 'g')
    plt.title('How much money ' + str(name) + ' lost')
    plt.xlabel("Round")
    plt.ylabel("winnings")
    plt.show()
    print()
