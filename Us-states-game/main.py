import turtle
import pandas as pd
from pathlib import Path

screen = turtle.Screen()
screen.title("U.S. States Game")

base_dir = Path(__file__).resolve().parent
image_path = base_dir / "blank_states_img.gif"
screen.addshape(str(image_path))
turtle.shape(str(image_path))

df = pd.read_csv(base_dir / "50_states.csv")

guessed_states = []
total_guesses = 0

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-280, 250)


def update_score():
    score_writer.clear()
    score_writer.write(
        f"Score: {len(guessed_states)}/{total_guesses}",
        align="left",
        font=("Arial", 12, "normal"),
    )


update_score()

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"Guess State - Score {len(guessed_states)}/{total_guesses}",
        prompt="Enter your guess or type 'Exit'",
    )
    if answer is None:
        break

    answer = answer.title()
    if answer.lower() == "exit":
        break

    total_guesses += 1
    condition = df[df["state"] == answer]
    if not condition.empty and answer not in guessed_states:
        guessed_states.append(answer)
        x_coor = condition["x"].iloc[0]
        y_coor = condition["y"].iloc[0]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coor, y_coor)
        t.write(answer, font=("Arial", 8, "normal"))

    update_score()

screen.exitonclick()
