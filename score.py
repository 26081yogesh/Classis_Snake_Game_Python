from turtle import Turtle

class Score(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.color("white")
      self.penup()
      self.goto(0, 270)
      
      self.write(f"Score :- {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
      self.hideturtle()

   def game_over(self):
      self.goto(0, 0)
      self.write("Game Over", move=False, align="center", font=('Arial', 24, 'normal'))

   def increase_score(self):
      self.score += 1
      self.clear()
      self.write(f"Score :- {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
      
