import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

game_on = True

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_correct = 0
guessed_states = []

while game_on:

    answer_state = screen.textinput(title=f"Guess the state: {states_correct}/50", prompt="whats another states name?").title()

    state_guess = answer_state

    if state_guess == "Exit":
        missing_states = []
        for state in df['state'].values:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if state_guess in df['state'].values:
        guessed_states.append(state_guess)
        state_data = df[df["state"] == state_guess]
        x = state_data["x"].iloc[0]
        y = state_data["y"].iloc[0]
        writer.goto(x, y)
        writer.write(state_guess)
        states_correct +=1




