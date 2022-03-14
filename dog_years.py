"""
dog years
"""


def main():
    total = 0
    while True:
        num = int(input("Enter a value: "))
        if num == 0:
            break
        total += num
        print("Running total is: " + str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
