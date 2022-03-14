"""
File: moon_weight.py
--------------------
Add your comments here.
"""
import random


def main():
    """
    8 ball
    """

    while True:
        eight_ball_function()


def eight_ball_function():
    input("ask a y or n question: ")
    answer = random.randint(1, 3)
    if answer == 1:
        print("no")
    if answer == 2:
        print("yes")
    if answer == 3:
        print("te voy a mata")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
