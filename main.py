import turtle
import pandas
screen = turtle.Screen()
screen.title("India States Guessing Game")
screen.setup(width=800, height=800)
image = "India-img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
screen.tracer(0)
count = 0
list_of_answers = []
while game_is_on:
    if count == 50:
        game_is_on = False
    data = pandas.read_csv("States_data.csv")
    answer_state = screen.textinput(title=f"{count}/{len(list(data.state))} Guess the state", prompt=" Guess the name of any state")
    user_guess = answer_state.title()
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    if user_guess == "Exit":
        list_of_not_answered = []
        for state in list(data.state):
            if state not in list_of_answers:
                list_of_not_answered.append(state)
        final_dictionary = {"State": list_of_not_answered}
        final_df = pandas.DataFrame(final_dictionary)
        final_df.to_csv("Unanswered_states.csv")

        game_is_on = False
        break
    if user_guess in list(data.state):
        if user_guess in list_of_answers:
            pass
        else:
            count += 1
            answer_row = (data[data.state == user_guess])
            x_position = int(answer_row.x)
            y_position = int(answer_row.y)
            tim.goto(x_position, y_position)
            tim.write(f"{user_guess}", font=("Courier", 8, "normal"))
            list_of_answers.append(user_guess)
    screen.update()
