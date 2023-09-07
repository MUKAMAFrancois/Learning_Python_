#

# the board
theBoard={
    'top-L':' ','top-M':'','top-R':'',

    'mid-L':' ','mid-M':'','mid-R':'',

    'low-L':' ', 'low-M':'', 'low-R':'',
}

def print_theboard(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print("--|--|--")

    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print("--|--|--")

    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")
    print("--|--|--")




# empty board
#print_theboard(theBoard)


def play(board):
    for i in range(9):
        position=input("which position?(top-L, top-M,top-R/ mid or low ):")
        entry=input(" first player (X) second player press enter:")
        if entry =="X":
            board[position]="X"
        else:
            board[position]="O"

       # board[position]=entry
        print_theboard(board=theBoard)

play(board=theBoard)
