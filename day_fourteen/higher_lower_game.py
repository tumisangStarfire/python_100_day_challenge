import random
import game_data
from art import logo,vs
# get game data list of things to compare
#randomly select the first A and B
#display infomation of each select choice
#use the number of follower count to create a comparission between the two. 
# if the user gueses right turn B into A and present a new A from the game data.
# keep the users current score, increae based on number of correct guesses

print(logo) 

def account_generator():
    return random.choice(game_data.data)

def display_account(data = {}): 
    return f'{ data["name"]}, {data["description"]}, from { data["country"] }'

def is_guess_right(guess = "",right_answer =""):
    if guess == right_answer:
        return True
    else:
        return False 

def right_answer(a_follower_count,b_follower_count): 
    """Purpose of this function is to compare two values together"""
    if a_follower_count > b_follower_count:
        return "A" 
    else:
        return "B"

def display_players(player_a = {}, player_b ={}):
    print(f"Compare A: { display_account(player_a) }")
    print(vs)
    print(f"Compare B: { display_account(player_b) }")

def play_game():  
    current_score = 0 #keeps the users game score
    player_a = account_generator()
    player_b = account_generator() 

    if player_a == player_b: 
        """To make sure the randomly generated accounts are not the same."""
        player_b = account_generator() 

    display_players(player_a,player_b)
    keep_playing = True 

    while keep_playing:  
        guess = input("who has more followers : Type 'A' or 'B': ") 
        answer =  right_answer(player_a["follower_count"],player_b["follower_count"])
        results = is_guess_right(guess,answer) 

        if player_a == player_b: 
            """To make sure the randomly generated accounts are not the same."""
            player_b = account_generator()

        if results: 
            if answer == 'A': 
                current_score += 1 
                player_b = account_generator()
                display_players(player_a,player_b)
                print(f"That is correct, current score : { current_score }")
            elif answer == 'B': 
                current_score += 1 
                player_a = player_b
                player_b = account_generator()
                display_players(player_a,player_b)
                print(f"That is correct, current score : { current_score }")
        else: 
            keep_playing = False
            print(f"That is wrong, final score : { current_score }")

play_game()
        


