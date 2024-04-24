import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.str.replace(" ", "").str.lower().to_list()
print(all_states)
collect_states = []

t = turtle.Turtle()
t.hideturtle()
t.penup()

while len(collect_states) <= 50:
    answer_state = screen.textinput(title=f"{len(collect_states)}/{len(all_states)} States Correct",
                                    prompt="What's another state's name?")
    if answer_state is None:
        break

    answer_state = answer_state.replace(" ", "").lower()

    if answer_state == "exit":
        for state in collect_states:
            print(state)
            i = all_states.index(state)
            data = data.drop(i)
        data.state.to_csv("states_to_learn.csv")
        break

    if not answer_state in collect_states and answer_state in all_states:

        i = all_states.index(answer_state)
        state_data = data.iloc[i]
        t.goto(state_data.x, state_data.y)
        t.write(state_data.state)
        collect_states.append(answer_state)
