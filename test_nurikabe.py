import nurikabe_copy
from testing_boards import *

def test_IsSolution():
    assert nurikabe_copy.IsSolution(testboard1) == False
    assert nurikabe_copy.IsSolution(testboard2) == False
    assert nurikabe_copy.IsSolution(testboard3) == False
    assert nurikabe_copy.IsSolution(testboard4) == True
    assert nurikabe_copy.IsSolution(testboard5) == False
    

def test_CanBeIsland():
    assert nurikabe_copy.CanBeIsland(testboard1,0,0) == False
    assert nurikabe_copy.CanBeIsland(testboard1,1,0) == True
    assert nurikabe_copy.CanBeIsland(testboard2,4,1) == True
    assert nurikabe_copy.CanBeIsland(testboard2,3,4) == False
    assert nurikabe_copy.CanBeIsland(testboard3,4,1) == False
    assert nurikabe_copy.CanBeIsland(testboard3,1,3) == False
    assert nurikabe_copy.CanBeIsland(testboard4,3,2) == False
    assert nurikabe_copy.CanBeIsland(testboard4,1,1) == False
    assert nurikabe_copy.CanBeIsland(testboard5,1,1) == True
    assert nurikabe_copy.CanBeIsland(testboard5,3,1) == False


'''
def test_solve():
'''