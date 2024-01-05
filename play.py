from human_engine import game
from ai import randomai, goodai
from humanvsai import humanvsai
from aivsai import aigame


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def engine():
    player1 = input("Who would you like to be the first player: ")
    player2 = input("Who would you like to be the second player: ")
    if player1 == player2 == "human":
        game()
    elif player2 == "random" and player1 == "human":
        humanvsai("X", randomai)
    elif player2 == "good" and player1 == "human":
        humanvsai("X", goodai)
    elif player1 == "random" and player2 == "random":
        aigame(randomai, randomai)
    elif player1 == "random" and player2 == "good":
        aigame(randomai, goodai)
    elif player1 == "good" and player2 == "random":
        aigame(goodai, randomai)
    elif player1 == "good" and player2 == "good":
        aigame(goodai, goodai)

engine()
    






    
