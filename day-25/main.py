import turtle
import pandas as pd
import score

end_counter = 50
current_counter = 0

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

score = score.Score()

dataframe = pd.read_csv("50_states.csv")


is_game_on = True
while is_game_on:
    data_input = screen.textinput(title=f"Guess the state {current_counter}/{end_counter}",
                                  prompt="Enter the state name:").title()
    if not dataframe[dataframe.state == data_input].empty:
        data = dataframe[dataframe.state == data_input]
        x = int(data.iloc[0].x)
        y = int(data.iloc[0].y)
        state = data.iloc[0].state
        score.state_write(x, y, state)
        dataframe.drop(data.index, inplace=True)
        current_counter += 1

    if current_counter == end_counter:
        is_game_on = False

    if data_input == "Exit":
        is_game_on = False


dataframe.state.to_csv("left.csv", index=False)