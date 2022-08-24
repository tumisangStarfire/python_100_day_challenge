import random
from art import logo
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


user_score = 0
computer_score = 0 
user_cards = []
computer_cards = [] 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  



def deal_card():  
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

def calculate_score(playing_cards= []):
    """Takes a list of Cards and returns the sum"""

    if sum(playing_cards) == 21 and len(playing_cards) == 2:
        return 0 

    if 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(playing_cards)

def compare(user_score, computer_score):
    """ The purpose of this function  is to compare the User Score and Computer Score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose,Computer has Black Jack" 
    elif user_score == 0:
        return "You win,you have Black Jack"
    elif user_score  > 21:
        return "You lose you went over" 
    elif computer_score  > 21:
        return "You win, Computer went over" 
    elif user_score > computer_score:
        return "You win" 
    else: 
        return "You win, Computer went over" 

for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

def play_game(): 
    print(logo) 
    is_game_over =  False
    while not is_game_over:
        
        user_score = calculate_score(user_cards)  
        computer_score = calculate_score(computer_cards) 
        print(f"Your cards : { user_cards } , current score { user_score }, \ncomputer's hand { computer_cards[0] } \n")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        
        else: 
            next_card = input("Type 'yes' to get another card, type 'n' to pass.\n").lower()

            if next_card == 'y':
                user_cards.append(deal_card())
            else: 
                is_game_over = True 

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"    Your final hand was { user_cards } and final score { user_score }")
    print(f"    Computer's hand is  { computer_cards } and score is { computer_score}")
    print(compare(user_score,computer_score))

restart = input("Do you want to play a game of BlackJack..? 'y' for yes or 'n' ").lower()
if restart == 'y':
    play_game()
    
        



        



