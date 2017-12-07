#first change

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def end(move):
    if move == 'quit':
        raise SystemExit
def checkBoard(board):
    if (board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-r'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['mid-L'] == 'X' and  board['mid-M'] == 'X' and board['mid-R'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X'):
        print('X is winner!')
        raise SystemExit
    elif (board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-r'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['mid-L'] == 'O' and  board['mid-M'] == 'O' and board['mid-R'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O'):
        print('O is winner!')
        raise SystemExit
    elif (board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O'):
        print('O is winner!')
        raise SystemExit
    
turn = 'X'
move = ' '
print('Type in "quit" to end game.')
print('\nTo choose a position, type in which row(top, mid, low) followed by which column(-R, -M, -L')
print('To move to the top left corner, you would type "top-L", bottom mid would be "low-M", without the quotes.')
while move != 'quit':
    printBoard(theBoard)
    checkBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    end(move)
    if (move not in theBoard):
        print('\nTry again.')
        continue
    elif (theBoard[move] == ' '):
        theBoard[move] = turn
    else:
        print('\nTry again.')
        continue
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    
