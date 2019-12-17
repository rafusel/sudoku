#Import libs
from random import randint
'''
SOLVER
'''
# Function that takes in the puzzle as a 2D array and returns the solution.
def solve(puzzle):
    backtrack = []
    i, j = 0, 0
    while (i < len(puzzle)):
        while (j < len(puzzle[i])):
            if (puzzle[i][j] == 0): # This is an element we may have to backtrack to.
                backtrack.append((i, j))

            if (len(backtrack) > 0 and backtrack[-1] == (i, j)): #We have to try and solve this element currently
                possibleElems = set() #Get a set of all the possible elements that we could solve with.
                for e in range(puzzle[i][j] + 1, 10): 
                    possibleElems.add(e)
                removeTaken(possibleElems, puzzle, i, j)
                
                if (len(possibleElems) > 0): # Does this element give us a possible solution
                    puzzle[i][j] = min(possibleElems)
                    j += 1
                
                else: #This element does not give a possible solution: backtrack
                    puzzle[i][j] = 0 #Reset the current element
                    backtrack.pop() #Remove this an element we need to backtrack to
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


'''
UTILITY FUNCTIONS
'''
#Parse a string version of the given input puzzle.
def parsePuzzle(stringPuzzle):
    puzzle = stringPuzzle.strip()
    puzzle = puzzle.split("\n")
    puzzle = [puzzle[i].split(" ") for i in range(len(puzzle))]
    return [list(map(lambda a: int(a), puzzle[i])) for i in range(len(puzzle))]

#Function to print the string representation of an 2D integer puzzle.
def printPuzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end="")
            print(" ", end="")
        print()


'''
TEST CASE FOR THE SOLVER
'''
puzzle = '''
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
'''

printPuzzle(parsePuzzle(puzzle))
print()
printPuzzle(solve(parsePuzzle(puzzle)))