# modules
# a module that checks after each move if there is a winner or not and returns the player who won.
from check import winner
import time


# functions
def printer(mode, the_print):
    with open('out.txt', mode) as f:
        f.write(the_print)


def run(arr):    # a function that prints the game or in other word it runs the game
    printer('w', '')
    for i in arr[::-1]:
        printer('a', f'{i}\n')


# variables
# a dictinoary that stores y axis for each column
num_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
players = [' ', 'x', 'o']
# a string that contains things that you can enter inputs, 1234567 for which column you want to place and * for exitting the game
arr = '1 2 3 4 5 6 7 * -'
player_indicator = 1
number_of_moves = 0
play_array = []    # an array that stores the moves x axis
state = True    # shows the state of the game if the game is still running or not
array = []    # the list of the map


# map
for i in range(6):
    array.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
run(array)    # running game before any move is made
printer('a', f'\n     Turn: Yellow | Indicator: x\n\n          total moves: {
        number_of_moves}')


# running the game
while state:

    # player
    player = players[player_indicator]

    # move input
    move = input(
        'to play you need to enter one of the 1234567 numbers and to exit * and to revert back one move - : ')
    while all(move != var for var in arr.split()):    # checks if the input provided is legal
        move = input(
            'error, please enter one of the 1234567 numbers or * , - : ')

    # game
    if move.isdigit():
        # move
        move = int(move)
        if num_dict[move] != 6:    # checks if the column you played your move is full or not
            array[num_dict[move]][move - 1] = player

            # checking winner
            # checks if there is a winner or not
            if_winner = winner(array, num_dict[move], move - 1)

            # run
            # if there is no winner print the move with the raining effect
            if if_winner != 'Yellow' and if_winner != 'Red':
                array[num_dict[move]][move - 1] = ' '
                # a loop for the raining effect
                for i in range(-5, (num_dict[move] - 1) * -1):
                    array[abs(i)][move - 1] = player
                    time.sleep(0.2)
                    run(array)
                    array[abs(i)][move - 1] = ' '
                array[num_dict[move]][move - 1] = player
                play_array.insert(0, move - 1)
                run(array)
                if player == 'o':
                    printer('a', f'\n     Turn: Yellow | Indicator: x\n\n          total moves: {
                            number_of_moves + 1}')
                elif player == 'x':
                    printer('a', f'\n     Turn: Red | Indicator: o\n\n          total moves: {
                            number_of_moves + 1}')

            else:    # if there is a winner prints the game one last time and prints who is the winner after all of that resets the out after 7 seconds
                state = False
                array[num_dict[move]][move - 1] = ' '
                for i in range(-5, (num_dict[move] - 1) * -1):
                    array[abs(i)][move - 1] = player
                    time.sleep(0.2)
                    run(array)
                    array[abs(i)][move - 1] = ' '
                array[num_dict[move]][move - 1] = player
                run(array)
                printer('a', f'\n       {if_winner} is the winner')
                time.sleep(7)
                printer('w', '')

            # things that needed to fix after a move was made
            num_dict[move] += 1
            player_indicator *= -1
            number_of_moves += 1
            if number_of_moves == 42:    # checks if its draw or not
                state = False
                run(array)
                printer('a', f'\n             Its a Draw!\n\n          total moves: {
                        number_of_moves}')
                time.sleep(3)
                printer('w', '')

        else:
            print(
                'error, please enter another number since the column you picked is already full')

    # stop and revert
    else:

        # revert
        if move == '-':
            try:
                num = play_array.pop(0)
                for i in range(num_dict[num + 1] - 1, 5):
                    array[i][num] = ' '
                    array[i + 1][num] = players[-1 * player_indicator]
                    run(array)
                    time.sleep(0.2)
                array[5][num] = ' '
                run(array)
                player_indicator *= -1
                num_dict[num + 1] -= 1
                number_of_moves -= 1
                if player == 'o':
                    printer('a', f'\n     Turn: Yellow | Indicator: x\n\n          total moves: {
                            number_of_moves}')
                elif player == 'x':
                    printer('a', f'\n     Turn: Red | Indicator: o\n\n          total moves: {
                        number_of_moves}')
            except:
                print('error, there is nothing to revert')

        # stop
        else:
            state = False
            printer('w', '')
