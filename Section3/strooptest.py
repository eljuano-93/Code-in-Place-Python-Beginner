"""
In psychology, the Stroop effect is a demonstration of cognitive interference where a delay in the
reaction time of a task occurs due to a mismatch in stimuli. The corresponding paper is one of
the most cited in the history of Psychology. In this section we are going to implement a working
version of a Stroop test. Our stroop test has two phases:
The first phase is the “control phase”. The user is shown color names written in the same
font-color. Each time the user has to write the name of the color. The program counts how many times they
type the name of the color correctly in 10 seconds.
The second phase is the “experiment phase”. The user is shown color names written in a font
color which is different from the color name. Each time the user has to write the name of the
font-color. The program counts how many times they type the name of the font-color correctly in 10 seconds.
"""

import random
import time
from termcolor import colored
from colorama import init
init(autoreset=True)
SECONDS = 10


def main():
    print_intro()
    input("Press Enter to continue...")
    print("-----PHASE 1-----")
    run_phase(True)
    print("-----PHASE 2-----")
    run_phase(False)


# Display tests counting the correct responses.
# The parameter is_phase_1 determines in which phase is set the function as a boolean condition.
# If this parameter is True the program runs as phase 1, if False as phase 2.
def run_phase(is_phase_1):
    correct_responses_counter = 0
    start = time.time()
    while time_counter(start, SECONDS):
        if is_phase_1:
            if run_single_test(True):
                correct_responses_counter += 1
        if not is_phase_1:
            if run_single_test(False):
                correct_responses_counter += 1
    print("End of the test.")
    print("Number of correct responses: " + str(correct_responses_counter))


# This function takes a starting point in time previously defined outside the function and counts up to another point.
# Returns a True boolean if the time elapsed is minor to the seconds defined as the lenght of time to count.
# In opposition it'll return a False boolean when the time elapsed reached the lenght of time to count.
def time_counter(start_time, seconds):
    current_time = time.time()
    time_elapsed = current_time - start_time
    return time_elapsed <= seconds


# Print welcome message and tests for font colors
def print_intro():
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('yellow', 'yellow')


# Display one experiment of printing a colored word and returning if the user gets the font color right
def run_single_test(is_phase_1):
    # print one colored word, match depending on is_phase_1 parameter
    color_name = random_color_name()
    font_color = get_font_color(color_name, is_phase_1)
    print_in_color(color_name, font_color)
    # get user answer  and return  if they  get  it right
    response = input("What color ink is the word written in? ")
    if response == font_color:
        return True
    else:
        print("Correct answer was " + str(font_color))
        return False


# get the color the text should be printed in - same as color_name if is_phase_1, or random if not
def get_font_color(color_name, should_match):
    if should_match:
        return color_name
    # make sure that color does not match color_name before returning
    font_color = random_color_name()
    while font_color == color_name:  # bad
        font_color = random_color_name()
    return font_color


# picks a random color name and returns it
def random_color_name():
    return random.choice(['red', 'blue', 'yellow'])


# print a text in the specified color
def print_in_color(text, font_color):
    # if font_color == 'pink': # magenta is a confusing name...
    #   font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
