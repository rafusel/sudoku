#Import libs
from random import choice

'''
SOLVER
'''
# Function that takes in the puzzle as a 2D array and returns the solution.
def fullSolve(puzzle):
    backtrack = []
    elemsTried = {}
    i, j = 0, 0
    while (i < len(puzzle)):
        while (j < len(puzzle[i])):
            if (puzzle[i][j] == 0): # This is an element we may have to backtrack to.
                backtrack.append((i, j))
                elemsTried[(i, j)] = set()

            if (len(backtrack) > 0 and backtrack[-1] == (i, j)): #We have to try and solve this element currently
                possibleElems = set() #Get a set of all the possible elements that we could solve with.
                for e in range(1, 10): 
                    possibleElems.add(e)
                removeTaken(possibleElems, puzzle, i, j) # Remove all the elements that occur in this row, column and box.
                possibleElems = possibleElems - elemsTried[(i, j)]
                
                if (len(possibleElems) > 0): # Does this element give us a possible solution
                    #puzzle[i][j] = min(possibleElems)
                    puzzle[i][j] = choice(tuple(possibleElems))
                    elemsTried[(i, j)].add(puzzle[i][j])
                    j += 1
                
                else: #This element does not give a possible solution: backtrack
                    puzzle[i][j] = 0 #Reset the current element
                    backtrack.pop() #Remove this an element we need to backtrack to
                    del elemsTried[(i, j)]
                    i, j = backtrack[-1] #Get the new values we need to backtrack to

            else: #Don't need to solve this one.
                j += 1
            
        i += 1
        j = 0 
    return puzzle

'''
FUNCTIONS USED BY SOLVER
'''
#Remove all taken elements in a given row, column and box.
def removeTaken(possibleElems, puzzle, i, j):
    checkRow(possibleElems, puzzle, i)
    checkCol(possibleElems, puzzle, j)
    checkBox(possibleElems, puzzle, i, j)

#Remove all elements in the ith row from possible elements.
def checkRow(possibleElems, puzzle, i):
    for j in range(len(puzzle[i])):
        possibleElems.discard(puzzle[i][j])

#Remove all elements in the jth column from possible element.
def checkCol(possibleElems, puzzle, j):
    for i in range(9):
        possibleElems.discard(puzzle[i][j])

#Remove all elements
def checkBox(possibleElems, puzzle, i, j):
    quadrant = (i//3, j//3) #Which quadrant is the current place in.
    for a in range(3):
        for b in range(3):
            possibleElems.discard(puzzle[a + 3 * quadrant[0]][b + 3 * quadrant[1]]) #Indexing trickery to get the indices in square.

