import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!") 
print("I am thinking of a number between 1 and 100")

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5 
attempts = 0  

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ") 

if difficulty == "easy":
    attempts = EASY_DIFFICULTY
elif difficulty == "hard": 
    attempts = HARD_DIFFICULTY

too_high_message = "Number is too high"
too_low_message = "Number is too low" 
you_lose_message = "You have run out of attempts you lose."


selection_numbers = []
for x in range(100): 
    """Create a list of numbers from 1-100"""
    selection_numbers.append(x)

random_number = random.choice(selection_numbers) 
end_game = False

while attempts > 0: 
    print(f"You have { attempts} attempts remaining, guess the number")
    guess = int(input("Make a guess: "))  
    attempts -= 1
    if guess == random_number:
        print(f"That is correct, you win, the answer is { random_number }")
        attempts = 0
        end_game == True
    elif guess > random_number:
        print(too_high_message) 
    elif guess < random_number:
        print(too_low_message) 
  
        

if attempts == 0:
    print(f"You lost the answer is: { random_number }")