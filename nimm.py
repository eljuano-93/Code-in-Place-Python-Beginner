"""
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. 
Players alternate taking stones until there are zero left. 
The game of Nimm goes as follows:
 1. The game starts with a pile of 20 stones between the players
 2. The two players alternate turns
 3. On a given turn, a player may take either 1 or 2 stone from the center pile
 4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""

NUM_OF_PLAYERS = 2


def main():

    
    num_of_stones_left = 20
    print("There are "+str(num_of_stones_left)+" stones left")

#   Player_turn variable keeps track of the user turn.
    while num_of_stones_left > 0:
        player_turn = 0
        while player_turn < NUM_OF_PLAYERS:
            player_turn += 1
            user_answer = int(input("Player "+str(player_turn)+" would you like to remove 1 or 2 stones? "))

#    If the player chooses another number different than 1 or 2 the programme enters in another loop
#    until he enters 1 or 2 again.
            while user_answer != 1 and user_answer != 2:
                user_answer = int(input("Please enter 1 or 2: "))
            if user_answer == 1:
                num_of_stones_left -= 1
            if user_answer == 2:
                num_of_stones_left -= 2
            print("There are " + str(num_of_stones_left) + " stones left")

#   When the number of stones reach 0 the programme announces the winner and ends.
            if num_of_stones_left == 0:
                if player_turn == 1:
                    print("Player "+str(player_turn + 1)+" wins.")
                if player_turn == 2:
                    print("Player "+str(player_turn - 1)+" wins.")
                break


#   There is a bag in the programme that I couldn't resolve yet. When variable NUM_OF_STONES_LEFT reaches
#   0, the player has the possibility to remove more quantity of stones than which are left. For example if
#   the stones left in the pile are 1, the player still can remove 2, therefore the programme will print
#   that there are -1 stones left.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
