from turtle import Turtle
FONT=("verdana",24,"normal")


class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.level=1
      self.hideturtle()
      self.penup()
      self.goto(-280, 250)
      self.update_score()
   def update_score(self):
      self.write(f"Level:{self.level}", align="left", font=FONT)

   def game_over(self):
      self.goto(0,0)
      self.write("GAME OVER", align="center", font=FONT)

   def increase_leevel(self):
      self.clear()
      self.level+=1
      self.update_score()