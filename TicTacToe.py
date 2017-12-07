#!/usr/bin/env python3
'''
A simple Tic-Tac-Toe Game in Python 3
'''

import os

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
winConditions = [['top-L','top-M','top-R'],
                 ['mid-L','mid-M','mid-R'],
                 ['low-L','low-M','low-R'],
                 ['top-L','mid-L','low-L'],
                 ['top-M','mid-M','low-M'],
                 ['top-R','mid-R','low-R'],
                 ['top-L','mid-M','low-R'],
                 ['low-L','mid-M','top-R']]
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def end(move):
    if move == 'quit':
        raise SystemExit
def checkBoard2(board):
    for winCond in winConditions:
        if (theBoard[winCond[0]] != ' ') and (theBoard[winCond[0]] == theBoard[winCond[1]] == theBoard[winCond[2]]):
            print('{} is the winner!'.format(theBoard[winCond[0]]))
            input('Press <Enter> to quit.')
            raise SystemExit

turn = 'X'
move = ' '

print('\nGood luck!\n')
while move != 'quit':
    print('Type in "quit" to end game.')
    print('\nTo choose a position, type in which row(top, mid, low) followed by which column(-R, -M, -L')
    print('To move to the top left corner, you would type "top-L", bottom mid would be "low-M", without the quotes.')
    printBoard(theBoard)
    checkBoard2(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    end(move)
    if (move not in theBoard):
        os.system('cls')
        print('\nTry again.\n')
        continue
    elif (theBoard[move] == ' '):
        theBoard[move] = turn
        os.system('cls')
        print('\nGood luck!\n')
    else:
        os.system('cls')
        print('\nTry again.\n')
        continue
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
