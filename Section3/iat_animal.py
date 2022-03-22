"""
In psychology, the Implicit Association Test (IAT) is a demonstration of cognitive interference
where a delay in the reaction time of a task occurs due to implicit associations users have. In this
section we are going to implement a working version of IAT to test associations of animals as
either cute or scary. Our IAT test has two phases:
The first phase is the “control phase”. The user is shown animal names with a stereotypical
association of cute or scary. Each time the user has to write the name of the association. Count
how many times they type the association correctly in 10 seconds.
The second phase is the “experiment phase”. The user is shown animal names with an
anti-stereotypical association. Each time the user has to write the name of the association. Count
how many times they type the association correctly in 10 seconds.
"""


import random
import time
SECONDS = 10


def main():
    print_intro(True)
    run_phase(True)
    print_intro(False)
    run_phase(False)


def print_intro(is_phase_1):
    if is_phase_1:
        print('Association test, standard')
    else:
        print('Association test, flipped')
    print('You will be asked to answer three questions.')
    print('You should associate animals as follows:')
    print('puppy', get_association('puppy', is_phase_1))
    print('panda', get_association('panda', is_phase_1))
    print('spider', get_association('spider', is_phase_1))
    print('bat', get_association('bat', is_phase_1))
    input('Press enter to start... ')


def random_animal():
    return random.choice(['puppy', 'panda', 'spider', 'bat'])


def get_association(animal, is_phase_1):
    if is_phase_1:
        if animal == 'puppy' or animal == 'panda':
            return 'cute'
        if animal == 'bat' or animal == 'spider':
            return 'scary'
    if not is_phase_1:
        if animal == 'puppy' or animal == 'panda':
            return 'scary'
        if animal == 'bat' or animal == 'spider':
            return 'cute'


def run_single_test(is_phase_1):
    # print one colored word, match depending on is_phase_1 parameter
    animal_name = random_animal()
    association = get_association(animal_name, is_phase_1)
    print(animal_name)
    # get user answer  and return  if they  get  it right
    response = input("Type the association: ")
    if response == association:
        return True
    else:
        print("Correct answer was " + association)
        return False


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


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()