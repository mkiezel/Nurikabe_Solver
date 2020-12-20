import copy
N = 5
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

states = []

'''
#plansza pokazuje odwiedzone rekurencyjnie wierzchołki
# 0 - nieodwiedzony
# 1 - odwiedzony
# "X" - nietykalny
plansza_odwiedzone = copy.deepcopy(plansza)

for i in range(0,N):
    for j in range(0,N):
        if plansza_odwiedzone[i][j] != 0: 
            plansza_odwiedzone[i][j] = "X"


plansza =   [["*", 1 ,"*", 1 ,"*"],
             ["*","*","*","*","*"],
             [ 3 ,"#","#","*", 3 ],
             ["*","*", "*" ,"*","#"],
             [ 3 ,"#","#", '*' ,"#"]]
'''

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

def solve(board):
    zeros = 0
    for row in range(0, N):
        for col in range(0, N):
            if board[row][col] == 0:
                if zeros == 0:
                    start = [row,col,[]]
                zeros += 1
    if CanBeIsland(board,start[0],start[1]) == True:
        start[2].append("#")
    if CanBeWater(board,start[0],start[1]) == True:
        start[2].append("*")
    passes = []
    passes.append(start)    
    while zeros != -1:
        zeros -= 1

        print(zeros)
        print(passes)
        
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
'''
def UsunOsobnaWode(plansza):
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] == "*":
                a = False


                if col > 0:
                    if plansza[row][col-1] == "*":
                        a= True
                if col < N-1:
                    if plansza[row][col+1] == "*":
                        a= True
                if row >0:
                    if plansza[row-1][col] == "*":
                        a= True
                if row < N-1:
                    if plansza[row+1][col] == "*":                  
                        a= True
                if a == False:
                    plansza[row][col] = 0
'''

def SolveRecursively(board):
    start = GetStart(board)
    print(start)
    recursion(start[0],start[1],start[2])


def recursion(row, col, options):
    global N, solution, board, states
    states.append([row,col])
    for i in range(0,len(board)):
        print(board[i])
    print (options)
    a = 0
    for i in range (0,N):
        if 0 in board[i]:
            a += 1
    if a==0:
        solution.append(copy.deepcopy(board))

    if options != []:
        board[row][col] = options[0]
        del options[0]
        if row > 0:
            if board[row-1][col] == 0:
                options2 = []
                if CanBeIsland(board,row-1,col) == True:
                    options2.append("#")
                if CanBeWater(board,row-1,col) == True:
                    options2.append("*")
                recursion(row-1,col,options2)


        if col < N-1:
            if board[row][col+1] == 0:
                options2 = []
                if CanBeIsland(board,row,col+1) == True:
                    options2.append("#")
                if CanBeWater(board,row,col+1) == True:
                    options2.append("*")
                recursion(row,col+1,options2)


        if row < N-1:
            if board[row+1][col] == 0:
                options2 = []
                if CanBeIsland(board,row+1,col) == True:
                    options2.append("#")
                if CanBeWater(board,row+1,col) == True:
                    options2.append("*")
                recursion(row+1,col,options2)


        if col > 0:
            if board[row][col-1] == 0:
                options2 = []
                if CanBeIsland(board,row,col-1) == True:
                    options2.append("#")
                if CanBeWater(board,row,col-1) == True:
                    options2.append("*")
                recursion(row,col-1,options2)


    if options != []:
        board[row][col] = options[0]
        del options[0]
        if row > 0:
            if board[row-1][col] == 0:
                options2 = []
                if CanBeIsland(board,row-1,col) == True:
                    options2.append("#")
                if CanBeWater(board,row-1,col) == True:
                    options2.append("*")
                recursion(row-1,col,options2)


        if col < N-1:
            if board[row][col+1] == 0:
                options2 = []
                if CanBeIsland(board,row,col+1) == True:
                    options2.append("#")
                if CanBeWater(board,row,col+1) == True:
                    options2.append("*")
                recursion(row,col+1,options2)


        if row < N-1:
            if board[row+1][col] == 0:
                options2 = []
                if CanBeIsland(board,row+1,col) == True:
                    options2.append("#")
                if CanBeWater(board,row+1,col) == True:
                    options2.append("*")
                recursion(row+1,col,options2)


        if col > 0:
            if board[row][col-1] == 0:
                options2 = []
                if CanBeIsland(board,row,col-1) == True:
                    options2.append("#")
                if CanBeWater(board,row,col-1) == True:
                    options2.append("*")
                recursion(row,col-1,options2)

    if col > 0:
        if board[row][col-1] == 0:
            board[row][col] = 0    

    if col < N-1:            
        if board[row][col+1]==0: 
            board[row][col] = 0

    if row > 0:
        if board[row-1][col]==0 :
            board[row][col] = 0

    if row < N-1:
        if board[row+1][col]==0:
            board[row][col] = 0

    '''
    if plansza[row][col] == "#" and CheckWholeIsland(plansza) == False:
        plansza[row][col] = 0

    UsunOsobnaWode(plansza)
    '''
    return False


#print(CheckSize(0,3,plansza))
# GÓRA PRAWO DÓŁ LEWO

print(CheckWater(board))

SolveRecursively(board)

print()
for i in range(0,len(board)):
    print(board[i])

print(solution)
print(states)