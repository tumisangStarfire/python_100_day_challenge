import random 

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''' 


paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''' 

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''' 

gamecon = [rock,paper,scissors] 

# Taking input from user choice  
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n => ")) 

print(f'Your choice')

# print game image by user choice  
print(gamecon[user_choice])  

computer_choice = random.randint(0,len(gamecon) -1) 

print(" Computer Choice: ")

# print game image by computer choice  
print(gamecon[computer_choice]) 

# rules in logic  
if user_choice == 0 and computer_choice == 2:  
    print("You win! 🎉")  
elif computer_choice == 0 and user_choice == 2:  
    print("You lose.  ☠")  
elif computer_choice > user_choice:  
    print("You lose. ☠")  
elif user_choice > computer_choice:  
    print("You win!🎉 ")  
elif computer_choice == user_choice:  
    print("It's a draw.")  
elif user_choice >= 3 or user_choice < 0:  
    print("You typed an invalid number, You Lose.  ☠")