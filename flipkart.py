def create_board(n,m):
    board=[[0 for c in range(m)] for r in range(n)]
    return board
def checkformovedown(board,n,m):
    #here we are checking for the board row movedown
    i=0
    j=0
    while i<n:
        while j<m:
            if board[i][j]==1:
                continue
            else:
                return board

        #if reach here means a row has all the 0
        #shift that downwards and all the row by one
        for r in range(1,n-1):
            for c in range(1,m-1):
                board[r][c]=board[r-1][c]
        #put 0 in top row
        for c in range(m):
            board[n-1][c]=0
    #return the updated board after move down or as it is
    return board


def print_board(board,n,m):
    for i in range(n):
        for j in range(m):
            print(board[i][j],end='')
        print()
#For shape Z
def board_for_Z(board, i, j, tetrimino, tversion):
    if tetrimino == 'Z' and tversion == 0:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i - 1][j + 1] = 1
        board[i - 1][j + 2] = 1
    if tetrimino == 'Z' and tversion == 1:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i + 1][j + 1] = 1
        board[i - 1][j] = 1
    return board

#For shape S
def board_for_S(board, i, j, tetrimino, tversion):
    if tetrimino == 'S' and tversion == 0:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i - 1][j + 1] = 1
        board[i - 1][j + 2] = 1
    if tetrimino == 'S' and tversion == 1:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i + 1][j] = 1
        board[i - 1][j + 1] = 1
    return board

#For shape T
def board_for_T(board, i, j, tetrimino, tversion):
    if tetrimino == 'T' and tversion == 0:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
        board[i + 1][j + 1] = 1
    if tetrimino == 'T' and tversion == 1:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 2][j + 2] = 1
        board[i + 1][j + 1] = 1
    if tetrimino == 'T' and tversion == 2:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 1][j - 1] = 1
        board[i + 1][j + 1] = 1
    if tetrimino == 'T' and tversion == 3:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
        board[i + 1][j + 1] = 1
    return board

#For shape L
def board_for_L(board, i, j, tetrimino, tversion):
    if tetrimino == 'L' and tversion == 0:
        board[i][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
        board[i + 1][j + 2] = 1
    if tetrimino == 'L' and tversion == 1:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 2][j] = 1
        board[i][j + 1] = 1
    if tetrimino == 'L' and tversion == 2:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 1][j + 1] = 1
        board[i + 1][j + 2] = 1
    if tetrimino == 'L' and tversion == 3:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 2][j] = 1
        board[i][j - 1] = 1
    return board

#For shape J
def board_for_J(board, i, j, tetrimino, tversion):
    if tetrimino == 'J' and tversion == 0:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
    if tetrimino == 'J' and tversion == 1:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
    if tetrimino == 'J' and tversion == 2:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i][j + 1] = 1
        board[i][j + 2] = 1
    if tetrimino == 'J' and tversion == 3:
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 2][j] = 1
        board[i + 2][j + 1] = 1
    return board

#For shape O
def board_for_O(board, i, j, tetrimino):
    print('board 0f o')
    if tetrimino == 'O':
        board[i][j] = 1
        board[i + 1][j] = 1
        board[i + 1][j + 1] = 1
        board[i][j + 1] = 1

    return board

#For shape I
def board_for_I(board, i, j, tetrimino, tversion):
    # fill the board for each shape
    if tetrimino == 'I' and tversion == 0:
        for c in (j, j + 4):
            board[i][c] = 1
    if tetrimino == 'I' and tversion == 1:
        for r in (i, i + 4):
            board[r][j] = 1
    print_board(board,n,m)
    return board





def boardwithSX(board,tetrimino,x,tversion):
   #ixj get i and j for given cordinate
   i,j=[int(k) for k in x.split('x')]

   # print(board)
   #for shape I
   board=board_for_I(board, i, j, tetrimino, tversion)

   #if the shape is O
   board=board_for_O(board, i, j, tetrimino)

   #if shape is J
   board=board_for_J(board, i, j, tetrimino, tversion)

   # if shape is L
   board=board_for_L(board, i, j, tetrimino, tversion)

   #for T shape
   board=board_for_T(board, i, j, tetrimino, tversion)

   #if shape is S
   board=board_for_S(board, i, j, tetrimino, tversion)

   #if shape is Z
   board=board_for_Z(board, i, j, tetrimino, tversion)

   board=checkformovedown(board,n,m)
   print_board(board,n,m)

   return  board

n=7
m=6
board=create_board(n,m)
board=boardwithSX(board,tetrimino='O',x='0x0',tversion=0)
board=boardwithSX(board,tetrimino='I',x='0x0',tversion=0)
board=boardwithSX(board,tetrimino='I',x='0x4',tversion=0)
# print_board(board,n,m)