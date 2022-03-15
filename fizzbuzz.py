"""
In the game Fizz Buzz, players take turns counting up from one. If a player’s turn lands on a
number that’s divisible by 3, she should say “fizz” instead of the number, and if it lands on a
number that’s divisible by 5, she should say “buzz” instead of the number. If the number is both
a multiple of 3 and of 5, she should say "fizzbuzz" instead of the number.
It is an interesting problem in control flow and parameter usage. Write a function called fizzbuzz
which accepts as a parameter an integer called n. The function should count up until and
including n, fizzing and buzzing the correct numbers along the way. Once it's done, the function
should return how many numbers were fizzed or buzzed along the way.
Next, complete your program by writing a main function that reads in an integer from the user
and plays fizzbuzz until it counts to the number.

Doctest:
>>> fizz_buzz(3)
1
2
Fizz
"""


def main():
    num_to_count = int(input("Number to count to: "))
    fizz_buzz(num_to_count)


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
