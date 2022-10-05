import turtle

import pandas

screen = turtle.Screen()


screen.title("Us States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
should_continue = True
correct_guesses = [] #TODO 7: change this to a dict
game_score = 0
number_of_states = len(data)


while len(correct_guesses) < 50:
    game_title = f"{game_score}/{number_of_states} Guess the state"
    state_input = screen.textinput(title=game_title, prompt="Name of the state:").title()
    state_guess = data[(data.state == state_input)]

    if state_input == "Exit":
       # missing_states = []
        all_states = data.state.to_list()
        #for state in all_states:
         #   if state not in correct_guesses:
          #      missing_states.append(state)
        missing_states = [state for state in all_states if state not in all_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.cvs")
        break

    if state_guess.empty:
        print("empty")
    else:
        state_name = state_guess.state
        x = state_guess.x
        y = state_guess.y
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(int(x), int(y))
        pen.write(state_input)
        correct_guesses.append(state_guess)
        game_score += 1


# TODO 1: Keep track of the number of states the user gets right, also show on the score on the textinput
# TODO 2: Write the name of the location using x,y coordinates
# TODO 3: Use a loop to allow the user to keep guessing
# TODO 4: Record the correct guesses in a list
# TODO 5: Compare the users correct guesses with the guesses they did not get right
# TODO 6: If state has already been guessed do not add the value to correct guesses or update the score



def get_mouse_click_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
