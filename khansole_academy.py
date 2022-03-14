"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
#  Number of correct responses to exit the loop.
NUM_IN_ROW = 3

"""
1 - Generate two random int of 2 digits OK
2 - Print the question OK
3 - Generate the loop in row
"""


def main():
    answer_counter = 1
    while answer_counter <= NUM_IN_ROW:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        total = 0
        operation = random.randint(1, 2)
        if operation == 1:
            total = num1 + num2
            print("What is "+str(int(num1))+" + "+str(int(num2))+"?")
        if operation == 2:
            total = num1 - num2
            print("What is "+str(int(num1))+" - "+str(int(num2))+"?")
        user_answer = int(input("Your answer: "))

        if user_answer == total:
            print("Correct! You've gotten "+str(answer_counter)+" correct in a row.")
            if answer_counter == NUM_IN_ROW:
                print("Congratulations! You mastered addition and subtraction.")
        answer_counter += 1

        if user_answer != total:
            answer_counter = 1
            print("Incorrect. The expected answer is "+str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
