

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0

    print("For reference, this is the numbering of the board: \n 7 | 8 | 9 \n 4 | 5 | 6 \n 1 | 2 | 3")


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        while int(move) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Please select a valid move")
            move = input()   

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
