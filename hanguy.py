# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:51:36 2022

@author: Asus
"""

import random
phase = ['''
  +---+
  | |
      |
      |
      |
      |
=========''', '''
  +---+
  | |
  O |
      |
      |
      |
=========''', '''
  +---+
  | |
  O |
  | |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /| |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
 / |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
 / \ |
      |
=========''']

#Animal word bank
hangman_game = ('ant baboon badger bat bear beaver camel cat clam cobra puma '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat'
         'goose hawk lion lizard llama mole monkey moose mouse mule newt'
         "otter owl panda parrot pigeon python rabbit ram rat raven"
         'rhino salmon seal shark sheep skunk sloth snake spider'
         'stork swan tiger toad trout turkey turtle weasel whale wolf'
         'wombat zebra').split()


random_choice = random.choice(hangman_game)

empty = ['_' for i in range(len(random_choice))]
print(' '.join(empty))

end_game = False
lives = 6

phase = phase[::-1]


while not end_game:
    user_choice = input('\nEnter your choice: ')

    if user_choice is empty:
      print(f'\now you guessed {user_choice}')
    
    for j in range(len(random_choice)):
        if user_choice in random_choice[j]:
            empty[j] = user_choice
      
    print(f'\n{" ".join(empty) }\n')

    
    if user_choice not in random_choice:
        lives-=1
        if lives == 0 :
            print('You lose.')
            print(f'Word is: {random_choice}')
            end_game = True
        
    print (phase[lives])
    
    
    if '_' not in empty:
        end_game = True
        print('You win.')