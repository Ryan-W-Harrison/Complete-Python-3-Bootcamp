# Tic Tac Toe Game


def display(row1, row2, row3):
    print(row1, flush=True)
    print(row2, flush=True)
    print(row3, flush=True)

    
def user_choice(player, y = None):
    if y is None:
        y = range(1, 10)

    choice = "WRONG"
    within_range = False
    while not within_range  or not choice.isdigit():
        choice = input(f'Player {player}, please enter a number (1-9): ')
        if not choice.isdigit():
            print("Sorry that is not a digit!")
        elif int(choice) not in y:
            print("Sorry that space is occupied!")
        else:
            within_range = True
    return int(choice)
  
def isxo(x):
    return x == "X" or x == "O"

def check_win(row1, row2, row3):
    wins = [
        (row1[0], row2[0], row3[0]),
        (row1[1], row2[1], row3[1]),
        (row1[2], row2[2], row3[2]),
        (row1[0], row1[1], row1[2]),
        (row2[0], row2[1], row2[2]),
        (row3[0], row3[1], row3[2]),
        (row1[0], row2[1], row3[2]),
        (row1[2], row2[1], row3[0])
    ]
    return any(all(isxo(cell) and cell == win[0] for cell in win) for win in wins)

def game():
    row1 = ['', '', '']
    row2 = ['', '', '']
    row3 = ['', '', '']
    
    game_over = False
    player = 1
    values = list(range(1, 10))
    while not game_over:
        display(row1, row2, row3)
        position = user_choice(y = values, player = player)
        mark = "X" if player == 1 else "0"
        if position in [1, 2, 3]:
            row1[position - 1] = mark
        elif position in [4, 5, 6]:
            row2[position - 4] = mark
        elif position in [7, 8, 9]:
            row3[position - 7] = mark

        values.remove(position)
      
        win = check_win(row1, row2, row3) 
        if win == True:
            print(f'Congratulations! Player {player} wins!')
            game_over = True
            display(row1, row2, row3)
        elif not values:
            print ('It\'s a tie!')
            game_over = True
        else:
            player = 3 - player
game()



        
        
        
        
