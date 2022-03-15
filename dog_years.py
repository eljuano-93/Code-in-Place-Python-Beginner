"""
dog years
Everyone knows that our furry friends age at a different rate than humans. Write a program that
asks the user for a human age (expressed as a whole number) and prints the equivalent dog age
using the fact that there are seven dog years per human year.
"""


def main():
    human_age = int(input("Enter an age in human years: "))
    print("The age in dog years is " + str(human_age * 7))


"""
Another way to do it defining a function

def main():
    human_age = int(input("Enter an age in human years: "))
    print("The age in dog years is " + str(dog_years_age(human_age)))


def dog_years_age(n):
    return n * 7
"""

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
