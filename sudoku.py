def sudoku_solve(board):
    print 'puzzle'
    for line in board:
        print line
    print
    for i in range(9):
        for j in range(9):
            if board[i][j]!=".":
               #print i,j
               if check(board,i,j,board[i][j]) == False:
                  return False
    print 'Valid Sudoku'
    emptyCells = getEmptyCells(board)
    print emptyCells
    ini_index = 0
    #counter = 0
    while ini_index!=len(emptyCells):
          x = emptyCells[ini_index][0]
          y = emptyCells[ini_index][1]
          #print x,y
          if board[x][y]==".":
             board[x][y] = "1"
          if check(board,x,y,board[x][y]):
             ini_index+=1
          elif int(board[x][y]) < 9:
               board[x][y] = str(int(board[x][y])+1)
          else:
               while(board[x][y]=="9"):
                     board[x][y]="."
                     if ini_index==0:
                        return False
                     ini_index-=1
                     x = emptyCells[ini_index][0]
                     y = emptyCells[ini_index][1]
               board[x][y] = str(int(board[x][y])+1)
             #else:
              #   if int(board[x][y]) < 9:
               #     board[x][y] = str(int(board[x][y]) + 1)
          #if counter%100000==0:
           #  print 'RUN-',counter
            # for line in board:
             #    print line
          #counter+=1
    print 'puzzle'
    for line in board:
        print line
    print
          #counter-=1
          #if counter == 0:
           #  return True
    return True
def check(board,x,y,val):
    for i in range(9):
        if i!=x and board[i][y] == val:
           return False
    for i in range(9):
        if i!=y and board[x][i] == val:
           return False
    sx = 3*(x/3)
    sy = 3*(y/3)
    ex = sx+3
    ey = sy+3
    for i in range(sx,ex):
        for j in range(sy,ey):
            if i!=x and j!=y and board[i][j]==val:
               return False
    return True
def getEmptyCells(board):
    emptyCells = []
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
              emptyCells.append([i,j])
    return emptyCells
sudoku = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9","7",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]

sudoku = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
#print check(sudoku,0,0,"1")
#print getEmptyCells(sudoku)
print sudoku_solve(sudoku)
