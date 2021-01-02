import copy
N = 4
global size, merge
size = 0
merge = 0
solution = []
test = True

board =[  [0, 1, 0, 1, 0], 
            [0, 0, 0, 0, 0],
            [3, 0, 0, 0, 3], 
            [0, 0, 0, 0, 0], 
            [3, 0, 0, 0, 0]]



board = [[1, 0, 0, 0],
[0, 0, 0, 3],
[2, 0, 0, 0],
[0, 0, 0, 2]]


'''
[0, 1, 0, 1, 0],      [█,1,█,1,█],
[0, 0, 0, 0, 0],      [█,█,█,█,█],
[3, 0, 0, 0, 3],      [3,░,░,█,3],
[0, 0, 0, 0, 0],      [█,█,█,█,░],
[3, 0, 0, 0, 0],      [3,░,░,█,░],
0 - unassigned field
* - river
# - island
'''
# we create 2 dimension array to save our deepness levels
deeps = []
for i in range(0,N):
    deeps.append([])
    for j in range(0,N):
        deeps[i].append(0)
act_deep = 0


options = []
for i in range(0,N):
    options.append([])
    for j in range(0,N):
        options[i].append([])



def CheckWater(board):
    global test
    row = 0
    col = 0
    test = True
    for row in range(0,N):
        for col in range(0,N):
            if board[row][col] == "*":
                break

        if board[row][col] == "*":
            break

    board2 = copy.deepcopy(board)
    SearchWater(row,col,board2)

    if test == False:
        return False

    for row in range(0, N):
        if "*" in board2[row]:
            return False
    
    return True
         
def SearchWater(row,col,board2):
    
    Check2x2(row,col)
    board2[row][col] = "x"

    if row > 0:
        if board2[row-1][col] == "*":
            board2[row-1][col] = "x"
            SearchWater(row-1,col,board2)

    if row < N-1:
        if board2[row+1][col] == "*":
            board2[row+1][col] = "x"
            SearchWater(row+1,col,board2)

    if col > 0:
        if board2[row][col-1] == "*":
            board2[row][col-1] = "x"
            SearchWater(row,col-1,board2)

    if col < N-1:
        if board2[row][col+1] == "*":
            board2[row][col+1] = "x"
            SearchWater(row,col+1,board2)

def Check2x2(row,col):
    global N, test

    if row < N - 1:
        if board[row+1][col] == "*":
            if col > 0:
                if board[row+1][col-1] == "*":
                    if board[row][col-1] == "*":
                        test = False

    if col < N-1:
        if board[row][col+1] == "*":
            if row < N-1:
                if board[row+1][col+1] == "*":
                    if board[row+1][col] == "*":  
                        test = False   

    if row > 0:
        if board[row-1][col] == "*":
            if col < N-1:
                if board[row-1][col+1] == "*":
                    if board[row][col+1] == "*":  
                        test = False

    if col >0:
        if board[row][col-1] == "*":
            if row >0:
                if board[row-1][col-1] == "*":
                    if board[row-1][col] == "*":  
                        test = False
  
def CheckSize(row,col,board2):
    global size, merge

    if row > 0:
        if board2[row-1][col] == "#":
            board2[row-1][col] = "x"
            size += 1
            CheckSize(row-1,col,board2)
        elif board2[row-1][col] not in [0,"*","#","x"]:
            merge = 1

    if row < N-1:
        if board2[row+1][col] == "#":
            board2[row+1][col] = "x"
            size += 1
            CheckSize(row+1,col,board2)
        elif board2[row+1][col] not in [0,"*","#","x"]:
            merge = 1

    if col > 0:
        if board2[row][col-1] == "#":
            board2[row][col-1] = "x"
            size += 1
            CheckSize(row,col-1,board2)
        elif board2[row][col-1] not in [0,"*","#","x"]:
            merge = 1

    if col < N-1:
        if board2[row][col+1] == "#":
            board2[row][col+1] = "x"
            size += 1
            CheckSize(row,col+1,board2)
        elif board2[row][col+1] not in [0,"*","#","x"]:
            merge = 1

def CheckIsland(board):
    global size, merge
    board2 = copy.deepcopy(board)
    for row in range(0, N):
        for col in range(0, N):
            if board[row][col] not in [0,"*","#"]:
                size = 1
                merge = 0
                board2[row][col] = "x"
                CheckSize(row,col,board2)
                if merge == 1:
                    return False    
                if size > board[row][col]:
                    return False
    for row in range(0, N):
        if "#" in board2[row]:
            return False
    return True

def CheckWholeIsland(board):
    global size, merge
    board2 = copy.deepcopy(board)
    islands = 0
    full = 0
    for row in range(0, N):
        for col in range(0, N):
            if board[row][col] not in [0,"*","#"]:
                islands += 1
                size = 1
                merge = 0
                board2[row][col] = "x"
                CheckSize(row,col,board2)
                if merge == 1:
                    return False    
                if size == board[row][col]:
                    full += 1
    for row in range(0, N):
        if "#" in board2[row]:
            return False
    if full == islands:
        return True
    return False

def CanBeWater(board, row, col):
    if board[row][col] != 0:
        return False
    board2 = copy.deepcopy(board)
    board2[row][col] = "*"
    return CheckWater(board2)

def CanBeIsland(board, row, col):
    if board[row][col] != 0:
        return False
    board2 = copy.deepcopy(board)
    board2[row][col] = "#"
    return CheckIsland(board2)

def GetOptions(board,row,col):
    options2 = []
    if CanBeIsland(board,row,col) == True:
        options2.append("#")
    if CanBeWater(board,row,col) == True:
        options2.append("*")
    return options2


def solve(board):
    start = GetStart(board)
    row = start[0]
    col = start[1]
    options[row][col] = start[2]
    act_deep = 1
    back_deep = 0
    max_deep = 0
    deeps[row][col] = act_deep
    solve = False
    while solve != True:
        solve = CheckWholeIsland(board)

        if options[row][col] != []:
            board[row][col] = options[row][col][0]
            #del options[row][col][0]
        #we are adding options
        if act_deep > max_deep:
            max_deep = act_deep

        if row > 0 and board[row-1][col] == 0 and GetOptions(board,row-1,col) !=[]:
            options[row-1][col] = GetOptions(board,row-1,col)
            act_deep += 1
            deeps[row-1][col] = copy.deepcopy(act_deep)
            row -= 1
            back_deep = 0

        elif col < N-1 and board[row][col+1] == 0 and GetOptions(board,row,col+1) !=[]:

            options[row][col+1] = GetOptions(board,row,col+1)
            act_deep += 1
            deeps[row][col+1] = copy.deepcopy(act_deep)
            col += 1
            back_deep = 0

        elif col > 0 and board[row][col-1] == 0 and GetOptions(board,row,col-1) !=[]:
            options[row][col-1] = GetOptions(board,row,col-1)
            act_deep += 1
            deeps[row][col-1] = copy.deepcopy(act_deep)
            col -= 1
            back_deep = 0

        elif row < N-1 and board[row+1][col] == 0 and GetOptions(board,row+1,col) !=[]:
            options[row+1][col] = GetOptions(board,row+1,col)
            act_deep += 1     
            deeps[row+1][col] = copy.deepcopy(act_deep)     
            row += 1   
            back_deep = 0       


        else: 
            back_deep -= 1
            for row2 in range(0,len(board)):
                for col2 in range(0,len(board)):
                    if deeps[row2][col2] == act_deep + back_deep:
                        row = row2
                        col = col2
            if 0 - back_deep == max_deep:
                print("trzeba zmienić")
                back_row = 0
                back_col = 0
                back_max = 0
                for row2 in range(0,len(board)):
                    for col2 in range(0,len(board)):
                        if deeps[row2][col2] > back_max and options[row2][col2] != []:
                            back_max = copy.deepcopy(deeps[row2][col2])
                            back_row = row2
                            back_col = col2

                for row2 in range(0,len(board)):
                    for col2 in range(0,len(board)):
                        if deeps[row2][col2] > back_max:
                            deeps[row2][col2] = 0
                            options[row2][col2] = []
                            board[row2][col2] = 0
                        elif deeps[row2][col2] == back_max:
                            board[row2][col2] = options[row2][col2][0]
                            del options[row2][col2][0]

                row = back_row
                col = back_col                     

    
        solve = CheckWholeIsland(board)


        


        for i in range(0,len(board)):
            print(board[i])

    








        
def GetStart(board):
    start = 0
    for row in range(0, N):
        for col in range(0, N):
            if board[row][col] == 0:
                    start = [row,col,[]]
                    break
        if start != 0:
            break
    if CanBeIsland(board,start[0],start[1]) == True:
        start[2].append("#")
    if CanBeWater(board,start[0],start[1]) == True:
        start[2].append("*")
    return start

def IsSolution(board):
    a = 0
    for i in range (0,N):
        if 0 in board[i]:
            a += 1
    if a==0:
        solution.append(copy.deepcopy(board))

def ClearBoard(deep_lvl):
    global board
    for row in range(0,N):
        for col in range(0,N):
            if deeps[row][col] > deep_lvl :
                deeps[row][col] = 0
                board[row][col] = 0


# GÓRA PRAWO DÓŁ LEWO
solve(board)






print("last deeps")
for i in range(0,len(board)):
    print(deeps[i])


print("last options")
for i in range(0,len(board)):
    print(options[i])


print()
for i in range(0,len(board)):
    print(board[i])

print(solution)


for i in range(0,len(solution)):
    if CheckWholeIsland(solution[i]) == True:
        print("JEST!!!!!!")

print(deeps)    
