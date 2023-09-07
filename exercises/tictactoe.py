
board=["-"]*9
current_player="X"
winner=None
game_running=True

# print the game board
def printBoard(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")


#printBoard(board=board)

#take player input

def PlayerInput(board):
    global current_player

    inp=int(input("Enter (0->8):"))
    if inp>=0 and inp<=8 and board[inp]=="-":
        board[inp]=current_player
        printBoard(board=board)
    else:
        print("Ooops! player exists in that place.")


# check win or tie
def check_horizontal(board):
    global winner

    if board[0]==board[1]==board[2] and board[1]!='-':
        winner=board[0]
        return True
    
    elif board[3]==board[4]==board[5] and board[5]!='-':
        winner=board[4]
        return True
    
    elif board[6]==board[7]==board[8] and board[5]!='-':
        winner=board[7]
        return True
    


def check_row(board):
    global winner

    if board[0]==board[3]==board[6] and board[3]!='-':
        winner=board[0]
        return True
    
    elif board[1]==board[4]==board[7] and board[1]!='-':
        winner=board[1]
        return True
    
    elif board[2]==board[5]==board[8] and board[8]!='-':
        winner=board[8]
        return True
    

def check_diagonal(board):
    global winner

    if board[0]==board[4]==board[8] and board[8]!='-':
        winner=board[4]
        return True
    
    elif board[2]==board[4]==board[6] and board[6]!='-':
        winner=board[6]
        return True
    

def check_tie(board):
    global game_running

    if "-" not in board:
        print("Finished")
        printBoard(board)
        game_running=False



#switch players

def switch_player():
    
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"


def check_win():

    global game_running
    if check_diagonal(board) or check_row(board) or check_horizontal(board):
        print("Winner is " + winner)
        game_running=False


    



#play

while game_running:
    printBoard(board)  
    PlayerInput(board=board)
    check_win()
    check_tie(board)
    switch_player()








