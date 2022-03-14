"""
fizzbuzz
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
