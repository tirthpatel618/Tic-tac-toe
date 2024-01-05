import random


def allpossiblemoves(board):
    possible_moves = []
    for i in range(1, 10):
        if board.get(str(i)) == ' ':
            possible_moves.append(str(i))
        else:
            pass
    return possible_moves

def winningmoves(board, turn):
    # top
    winmoves = []
    if board['7'] == board['8'] == turn:
        winmoves.append("9")
    elif board['8'] == board['9'] == turn:
        winmoves.append("7")
    elif board['7'] == board['9'] == turn:
        winmoves.append("8")
    #middle
    if board['4'] == board['5'] == turn:
        winmoves.append("6")
    elif board['5'] == board['6'] == turn:
        winmoves.append("4")
    elif board['4'] == board['6'] == turn:
        winmoves.append("5")
    #bottom
    if board['1'] == board['2'] == turn:
        winmoves.append("3")
    elif board['2'] == board['3'] == turn:
        winmoves.append("1")
    elif board['1'] == board['3'] == turn:
        winmoves.append("2")
    #left
    if board['7'] == board['4'] == turn:
        winmoves.append("1")
    elif board['4'] == board['1'] == turn:
        winmoves.append("7")
    elif board['7'] == board['1'] == turn:
        winmoves.append("4")
    #mid
    if board['8'] == board['5'] == turn:
        winmoves.append("2")
    elif board['2'] == board['5'] == turn:
        winmoves.append("8")
    elif board['8'] == board['2'] == turn:
        winmoves.append("5")
    #right
    if board['9'] == board['6'] == turn:
        winmoves.append("3")
    elif board['3'] == board['6'] == turn:
        winmoves.append("9")
    if board['9'] == board['3'] == turn:
        winmoves.append("6")
    #down diagnol
    if board['7'] == board['5'] == turn:
        winmoves.append("3")
    elif board['5'] == board['3'] == turn:
        winmoves.append("7")
    elif board['7'] == board['3'] == turn:
        winmoves.append("5")
    #up diagnol
    if board['1'] == board['5'] == turn:
        winmoves.append("9")
    elif board['5'] == board['9'] == turn:
        winmoves.append("1")
    elif board['1'] == board['9'] == turn:
        winmoves.append("5")
    return winmoves
    

def randomai(board, player, count):
    possible_moves = allpossiblemoves(board)
    move = ""
    winmoves = list(filter(lambda x: (x in possible_moves), winningmoves(board, player)))

    if len(winmoves) == 0:
        move = random.choice(possible_moves)
    else:
        move = random.choice(winmoves)
    return move



def goodai(board, player, count):
    possible_moves = allpossiblemoves(board)
    winmoves = list(filter(lambda x: (x in possible_moves), winningmoves(board, player)))
    if player == "O":
        otherwinmoves = list(filter(lambda x: (x in possible_moves), winningmoves(board, "X")))
    else:
        otherwinmoves = list(filter(lambda x: (x in possible_moves), winningmoves(board, "O")))
    
    if count == 1:
        move = "4"
    elif count == 2 and '9' in possible_moves:
        move = "9"
    else:
        if len(winmoves) != 0:
            move = random.choice(winmoves)
        else:
            if len(otherwinmoves) != 0:
                move = random.choice(otherwinmoves)
            else:
                move = random.choice(possible_moves)
    return move

        
        


    


    


        

