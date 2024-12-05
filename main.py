from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

#creating the screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

#creating object from class Score, Snake and Food
score = Score()
snake = Snake()
food = Food()

#for controlling the movement of snake by keyboard
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    #to increment the length of snake when it hit on food and update the score
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.inc_score()
        
    #to check the hit on the boundary by snake and make game over
    if snake.head.xcor() > 290 or  snake.head.xcor() < -290 or snake.head.ycor() > 290 or  snake.head.ycor() < -290:
        is_game_on = False 
        score.game_over()
    
    #to check the hit on it's own body and make game over
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()
       

screen.exitonclick()