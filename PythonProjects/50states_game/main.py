from turtle import Screen, Turtle
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
# screen.bgpic('blank_states_img.gif')
screen.setup(width=800, height=550)
screen.addshape(image)
turtle.shape(image)

# Gets the x and y co-ordinates of the point where the mouse is clicked
# def get_mouse_click_co_or(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_co_or)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="Input the state's name").title()
    print(answer_state)

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
#       all_states.remove(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
#       t.write(answer_state)
        t.write(state_data.state.item())

data = pandas.DataFrame(missed_states)
data.to_csv("states_to_learn.csv", index=False)


# Keeps the screen on even after click
# turtle.mainloop
# screen.exitonclick()
