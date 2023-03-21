#Tic Tac Toe

print('Welcome to Tic_Tac_Toe Game!')
print("BRANCH COMMIT CHANGE")

#board
board = [['_','_','_'],['_','_','_'],['_','_','_']]

#function that draws the board
def drawBoard():
    print('-' * 10)
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + '     1.1 | 1.2 | 1.3')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + '     2.1 | 2.2 | 2.3')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + '     3.1 | 3.2 | 3.3')
    print('-' * 10)                         #the 1.1,2.2 matrix only for a player comfort

#turn of X player
def xTurn():
    valid = False
    while not valid:
        player_answer1 = input('Please choose a string: ')
        player_answer1 = int(player_answer1) - 1
        if player_answer1 >= 0 and player_answer1 < 3:  #cheking if player choosed correct number
            player_answer2 = input('Please choose a column: ')
            player_answer2 = int(player_answer2) - 1
            if player_answer2 >= 0 and player_answer2 < 3:
                if str(board[player_answer1][player_answer2]) not in 'XO':
                    board[player_answer1][player_answer2] = 'X'
                    valid = True
                else:
                    print('The cell is already choosen, take anoter!')
            else:
                print('Please write a number from 1 to 3')
        else:
            print('Please write a number from 1 to 3')

#turn of O player
def oTurn():
    valid = False
    while not valid:
        player_answer1 = input('Please choose a string: ')
        player_answer1 = int(player_answer1) - 1
        if player_answer1 >= 0 and player_answer1 < 3:
            player_answer2 = input('Please choose a column: ')
            player_answer2 = int(player_answer2) - 1
            if player_answer2 >= 0 and player_answer2 < 3:
                if str(board[player_answer1][player_answer2]) not in 'XO':
                    board[player_answer1][player_answer2] = 'O'
                    valid = True
                else:
                    print('The cell is already choosen, take anoter!')
            else:
                print('Please write a number from 1 to 3')
        else:
            print('Please write a number from 1 to 3')

#function checks who win
def checkWin():
    global whowin
    for i in board:
        if board[0][0] == board[0][1] == board[0][2] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[1][0] == board[1][1] == board[1][2] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[2][0] == board[2][1] == board[2][2] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][0] == board[1][0] == board[2][0] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][1] == board[1][1] == board[2][1] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][2] == board[1][2] == board[2][2] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][0] == board[1][0] == board[2][0] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[0][1] == board[1][1] == board[2][1] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[0][2] == board[1][2] == board[2][2] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[0][0] == board[0][1] == board[0][2] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[1][0] == board[1][1] == board[1][2] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[2][0] == board[2][1] == board[2][2] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[0][0] == board[1][1] == board[2][2] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][0] == board[1][1] == board[2][2] in 'O':
            win = True
            whowin = 'O'
            return win
        elif board[0][2] == board[1][1] == board[2][0] in 'X':
            win = True
            whowin = 'X'
            return win
        elif board[0][2] == board[1][1] == board[2][0] in 'O':
            win = True
            whowin = 'O'
            return win
        else:
            win = False
            return win

#main game function
def game():
    counter = 0
    while checkWin() == False:
        drawBoard()
        if counter % 2 == 0:
            xTurn()
        else:
            oTurn()
        counter += 1
        checkWin()
        if counter == 9:                #if no one wins till 9 move, it's a draw
            drawBoard()
            print('DRAW')
            break
        elif checkWin() == False:
            continue
        else:
            drawBoard()
            print(f'We have a winner! {whowin} won!')

game()