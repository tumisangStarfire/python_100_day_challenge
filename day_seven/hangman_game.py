import random
from hangman_words import word_list
from hangman_art import stages,logo
import hangman_art
print("Welcome to the hangman game")

#TODO-0: - Import the logo from hangman_art.py and print it at the start of the game. 
print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
final_word = []
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

number_of_letters = len(chosen_word)
number_of_tries = 6 
placeholder = "_"
end_of_game = False

for i in range(number_of_letters): 
    final_word.append(placeholder)
    
while not end_of_game :
  guess_letter = input("Guess the letter\n").lower()
     
  if guess_letter in chosen_word:
    print(f"You've already guessed {guess_letter}")

  for position in range(number_of_letters):   
    letter = chosen_word[position]
    if guess_letter == letter: 
      final_word[position] = letter

  if placeholder not in final_word:
    print("You have won" ,final_word)  
  else: 
    number_of_tries -= 1 
    print(stages[number_of_tries])
            



#TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

        






