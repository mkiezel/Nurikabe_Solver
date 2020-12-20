import copy
N = 5
global size, lacza, test
size = 0
lacza = 0
rozwiazanie = []
test = True
#plansza = [[0] * N] * N
plansza =[  [0, 1, 0, 1, 0], 
            [0, 0, 0, 0, 0],
            [3, 0, 0, 0, 3], 
            [0, 0, 0, 0, 0], 
            [3, 0, 0, 0, 0]]

stany = []
#plansza pokazuje odwiedzone rekurencyjnie wierzchołki
# 0 - nieodwiedzony
# 1 - odwiedzony
# "X" - nietykalny
plansza_odwiedzone = copy.deepcopy(plansza)

for i in range(0,N):
    for j in range(0,N):
        if plansza_odwiedzone[i][j] != 0: 
            plansza_odwiedzone[i][j] = "X"

'''
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
0 - jest to startowe pole - nie wiadomo
inne cyfry - początkowe wartości
* - rzeka
# - ląd
'''

# sprawdza wszystkie założenia dla wody
def CzyWoda(plansza):
    ile = 0
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] == '*':
                ile += 1
    if ile < 2:
        return True
    
    for row in range(0, N):
        for col in range(0, N):



            if plansza[row][col] == "*":
                sum = 0

                if row < N - 1:
                    if plansza[row+1][col] == "*":
                        sum += 1
                        if col > 0:
                            if plansza[row+1][col-1] == "*":
                                if plansza[row][col-1] == "*":
                                    return False

                if col < N-1:
                    if plansza[row][col+1] == "*":
                        sum += 1
                        if row < N-1:
                            if plansza[row+1][col+1] == "*":
                                if plansza[row+1][col] == "*":  
                                    return False    

                if row > 0:
                    if plansza[row-1][col] == "*":
                        sum += 1
                        if col < N-1:
                            if plansza[row-1][col+1] == "*":
                                if plansza[row][col+1] == "*":  
                                    return False

                if col >0:
                    if plansza[row][col-1] == "*":
                        sum += 1
                        if row >0:
                            if plansza[row-1][col-1] == "*":
                                if plansza[row-1][col] == "*":  
                                    return False                                    

                if sum == 0 or sum == 4:
                    return False
    return True

def CzyWoda2(board):
    row = 0
    col = 0
    test = True
    while board[row][col] != "*":
        while board[row][col] != "*":
            if col < N:
                col += 1
            else:
                col = 0
                break
        if row < N:
            row += 1
        else:
            return True

    board2 = copy.deepcopy(board)
    SearchWater(row,col,plansza2)

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
    global N, test, plansza
    if row < N - 1:
        if plansza[row+1][col] == "*":
            if col > 0:
                if plansza[row+1][col-1] == "*":
                    if plansza[row][col-1] == "*":
                        test = False

    if col < N-1:
        if plansza[row][col+1] == "*":
            if row < N-1:
                if plansza[row+1][col+1] == "*":
                    if plansza[row+1][col] == "*":  
                        test = False   

    if row > 0:
        if plansza[row-1][col] == "*":
            if col < N-1:
                if plansza[row-1][col+1] == "*":
                    if plansza[row][col+1] == "*":  
                        test = False

    if col >0:
        if plansza[row][col-1] == "*":
            if row >0:
                if plansza[row-1][col-1] == "*":
                    if plansza[row-1][col] == "*":  
                        test = False



# rekurencyjnie idzie "w głąb" wyspy szuka innych cyfr i zlicza jej rozmiar
def sprawdzrozmiar(row,col,plansza2):
    global size, lacza

    if row > 0:
        if plansza2[row-1][col] == "#":
            plansza2[row-1][col] = "x"
            size += 1
            sprawdzrozmiar(row-1,col,plansza2)
        elif plansza2[row-1][col] not in [0,"*","#","x"]:
            lacza = 1

    if row < N-1:
        if plansza2[row+1][col] == "#":
            plansza2[row+1][col] = "x"
            size += 1
            sprawdzrozmiar(row+1,col,plansza2)
        elif plansza2[row+1][col] not in [0,"*","#","x"]:
            lacza = 1

    if col > 0:
        if plansza2[row][col-1] == "#":
            plansza2[row][col-1] = "x"
            size += 1
            sprawdzrozmiar(row,col-1,plansza2)
        elif plansza2[row][col-1] not in [0,"*","#","x"]:
            lacza = 1

    if col < N-1:
        if plansza2[row][col+1] == "#":
            plansza2[row][col+1] = "x"
            size += 1
            sprawdzrozmiar(row,col+1,plansza2)
        elif plansza2[row][col+1] not in [0,"*","#","x"]:
            lacza = 1

# sprawdza wszystkie założenia dla lądu
def CzyLad(plansza):
    global size, lacza
    plansza2 = copy.deepcopy(plansza)
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] not in [0,"*","#"]:
                size = 1
                lacza = 0
                plansza2[row][col] = "x"
                sprawdzrozmiar(row,col,plansza2)
                if lacza == 1:
                    return False    
                if size > plansza[row][col]:
                    return False
    for row in range(0, N):
        if "#" in plansza2[row]:
            return False
    return True

def CzyCalyLad(plansza):
    global size, lacza
    plansza2 = copy.deepcopy(plansza)
    wyspy = 0
    pelne = 0
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] not in [0,"*","#"]:
                wyspy += 1
                size = 1
                lacza = 0
                plansza2[row][col] = "x"
                sprawdzrozmiar(row,col,plansza2)
                if lacza == 1:
                    return False    
                if size == plansza[row][col]:
                    pelne += 1
    for row in range(0, N):
        if "#" in plansza2[row]:
            return False
    if pelne == wyspy:
        return True
    return False

def CzyMoznaWoda(planszax, row, col):
    if planszax[row][col] != 0:
        return False
    planszay = copy.deepcopy(planszax)
    planszay[row][col] = "*"
    return CzyWoda(planszay)

def CzyMoznaLad(planszax, row, col):
    if planszax[row][col] != 0:
        return False
    planszay = copy.deepcopy(planszax)
    planszay[row][col] = "#"
    return CzyLad(planszay)

def rozwiaz(plansza):
    zera = 0
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] == 0:
                if zera == 0:
                    start = [row,col,[]]
                zera += 1
    if CzyMoznaLad(plansza,start[0],start[1]) == True:
        start[2].append("#")
    if CzyMoznaWoda(plansza,start[0],start[1]) == True:
        start[2].append("*")
    przejscia = []
    przejscia.append(start)    
    while zera != -1:
        zera -= 1

        print(zera)
        print(przejscia)
        
def dajstart(plansza):
    start = 0
    for row in range(0, N):
        for col in range(0, N):
            if plansza[row][col] == 0:
                    start = [row,col,[]]
                    break
        if start != 0:
            break
    if CzyMoznaLad(plansza,start[0],start[1]) == True:
        start[2].append("#")
    if CzyMoznaWoda(plansza,start[0],start[1]) == True:
        start[2].append("*")
    return start

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


def rozwiazrekurencyjnie(plansza):
    start = dajstart(plansza)
    print(start)
    rekurencyjnie(start[0],start[1],start[2])

def rekurencyjnie(row, col, opcje):
    global N, rozwiazanie, plansza, stany
    stany.append([row,col])
    for i in range(0,len(plansza)):
        print(plansza[i])
    print (opcje)
    a = 0
    for i in range (0,N):
        if 0 in plansza[i]:
            a += 1
    if a==0:
        rozwiazanie.append(copy.deepcopy(plansza))

    if opcje != []:
        plansza[row][col] = opcje[0]
        del opcje[0]
        if row > 0:
            if plansza[row-1][col] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row-1,col) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row-1,col) == True:
                    opcje2.append("*")
                rekurencyjnie(row-1,col,opcje2)


        if col < N-1:
            if plansza[row][col+1] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row,col+1) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row,col+1) == True:
                    opcje2.append("*")
                rekurencyjnie(row,col+1,opcje2)


        if row < N-1:
            if plansza[row+1][col] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row+1,col) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row+1,col) == True:
                    opcje2.append("*")
                rekurencyjnie(row+1,col,opcje2)


        if col > 0:
            if plansza[row][col-1] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row,col-1) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row,col-1) == True:
                    opcje2.append("*")
                rekurencyjnie(row,col-1,opcje2)

    print ("opcje po jednym",opcje)


    if opcje != []:
        plansza[row][col] = opcje[0]
        del opcje[0]
        if row > 0:
            if plansza[row-1][col] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row-1,col) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row-1,col) == True:
                    opcje2.append("*")
                rekurencyjnie(row-1,col,opcje2)


        if col < N-1:
            if plansza[row][col+1] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row,col+1) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row,col+1) == True:
                    opcje2.append("*")
                rekurencyjnie(row,col+1,opcje2)


        if row < N-1:
            if plansza[row+1][col] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row+1,col) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row+1,col) == True:
                    opcje2.append("*")
                rekurencyjnie(row+1,col,opcje2)


        if col > 0:
            if plansza[row][col-1] == 0:
                opcje2 = []
                if CzyMoznaLad(plansza,row,col-1) == True:
                    opcje2.append("#")
                if CzyMoznaWoda(plansza,row,col-1) == True:
                    opcje2.append("*")
                rekurencyjnie(row,col-1,opcje2)

    if col > 0:
        if plansza[row][col-1] == 0:
            plansza[row][col] = 0    

    if col < N-1:            
        if plansza[row][col+1]==0: 
            plansza[row][col] = 0

    if row > 0:
        if plansza[row-1][col]==0 :
            plansza[row][col] = 0

    if row < N-1:
        if plansza[row+1][col]==0:
            plansza[row][col] = 0

    '''
    if plansza[row][col] == "#" and CzyCalyLad(plansza) == False:
        plansza[row][col] = 0

    UsunOsobnaWode(plansza)
    '''
    return False


#print(sprawdzrozmiar(0,3,plansza))
# GÓRA PRAWO DÓŁ LEWO

rozwiazrekurencyjnie(plansza)


print()
for i in range(0,len(plansza)):
    print(plansza[i])

print(rozwiazanie)
print(stany)