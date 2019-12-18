from solver import fullSolve
from random import randint

#Function to generate a solvable sudoku puzzle. Returns 2D int list.
def generatePuzzle():
    #Create a solved puzzle
    zeroes = [[0 for i in range(9)] for i in range(9)]
    solveablePuzzle = fullSolve(zeroes)
    nRemove = randint(40, 60) #Remove between 40 and 60 elements.
    
    toRemove = set() #Create a set of indices to remove
    while (len(toRemove) < nRemove):
        i, j  = (randint(0, 8), randint(0, 8))
        if (not (i, j) in toRemove):
            toRemove.add((i, j))

    for _ in range(nRemove): #Remove the set indices by setting to zero
        i, j = toRemove.pop()
        solveablePuzzle[i][j] = 0
    
    return solveablePuzzle