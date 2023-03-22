import turtle
import random

# Create turtle window and set background color
window = turtle.Screen()
window.bgcolor("light blue")

# Create turtle to draw balls
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")


# Function to draw n balls
def draw_balls(n):
    ball.clear()
    for i in range(n):
        ball.penup()
        ball.goto((i - n / 2) * 50, 0)
        ball.pendown()
        ball.stamp()


# Function to get valid number of balls from user
def get_num_balls():
    while True:
        n = int(input("Enter number of balls (must be 15 or more): "))
        if n >= 15:
            return n


# Function to get valid number of balls to remove from user
def get_num_remove(n):
    while True:
        k = int(input("Enter number of balls to remove (1-4): "))
        if 1 <= k <= 4 and k <= n:
            return k
        else:
            print(f"Only {n} balls are left! \nEnter number of balls to remove (1-{n}): ")


# Function to get number of balls to remove by computer
def get_computer_move(n):
    if (n - 1) % 5 == 0:
        return random.randint(1, 4)
    else:
        return (n - 1) % 5


# Main function to play game
def play_game():
    n = get_num_balls()
    draw_balls(n)
    while n > 0:
        # Human player's turn
        print("Your turn...")
        k = get_num_remove(n)
        n -= k
        draw_balls(n)
        if n == 0:
            print("You win!")
            break
        # Computer's turn
        print("Computer's turn...")
        k = get_computer_move(n)
        print("Computer removes", k, "balls")
        n -= k
        draw_balls(n)
        if n == 0:
            print("Computer wins!")
            break


# Play the game
play_game()

# Exit window on click
window.exitonclick()
