"""
HANGMAN GAME
output format:
Let's play Hangman!!
You hava only 6 lives. Try to guess the word within 6 attemps.
GOOD LUCK!
"""

import random
import word_list
import hangman_stages

print("Let's play Hangman!!\nYou hava only 6 lives. Try to guess the word within 6 attemps.\nGOOD LUCK!")
random_word=random.choice(word_list.words)
display=[]
lives=6

for i in range(0,len(random_word)):
    display+='_'
print(display)

game_over=False

while not game_over:
    guessed_letter=input("Guess a letter:")
    for i in range(0, len(random_word)):
        letter=random_word[i]
        if letter==guessed_letter:
            display[i]=guessed_letter
    print(display)
    if guessed_letter not in random_word:
        lives=lives-1
        print(hangman_stages.stages[lives])
        if lives==0:
            print("Game over! You lose")
            print(f"correct word is {random_word}")
            game_over=True
    if '_' not in display:
        game_over=True
        print("Congratulations! You have guessed the corrected word")
