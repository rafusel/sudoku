#Import libs
from random import randint

# Function that takes in the puzzle as a 2D array and returns the solution.
def solve(puzzle):
    backtrack = []
    i, j = 0, 0
    while (i < len(puzzle)):
        while (j < len(puzzle[i])):
            print(i, j)
            if (puzzle[i][j] == 0): # This is an element we have to solve
                puzzle[i][j] = 1
                backtrack.append((i, j))
            if (checkRow(puzzle, i) and checkCol(puzzle, j) and checkBox(puzzle, i, j)): # Does this element give us a possible solution
                j += 1
            else: #This element does not give a possible solution: backtrack
                puzzle[i][j] = 0 #Reset the current element
                backtrack.pop() #Remove this an element we need to backtrack to
                i, j = backtrack.pop() #Get the new values we need to backtrack to
                if (puzzle[i][j] < 9):
                    puzzle[i][j] += 1 #Increment the value we are backtracking to
                    #TODO need to make this conditional based on if there's a repeat in the row, col, box
                else: 
                    return "No solution"
        i += 1
        j = 0 
    return puzzle

#Remove all elements in the ith row from possible elements.
def checkRow(possibleElems, puzzle, i):
    for elem in puzzle[i]:
        possibleElems.remove(elem)

#Remove all elements in the jth column from possible element.
def checkCol(possibleElems, puzzle, j):
    for i in range(9):
        possibleElems.remove(puzzle[i][j])

#Remove all elements
def checkBox(possibleElems, puzzle, i, j):
    quadrant = ((i//3) + 1, (j//3) + 1) #Which quadrant is the current place in.
    for a in range(1, 4):
        for b in range(1, 4):
            possibleElems.remove(puzzle[a * quadrant[0] - 1][b * quadrant[1] - 1]) #Indexing trickery to get the indices in square.

#Parse a string version of the given input puzzle.
def parsePuzzle(stringPuzzle):
    puzzle = stringPuzzle.strip()
    puzzle = puzzle.split("\n")
    puzzle = [puzzle[i].split(" ") for i in range(len(puzzle))]
    return [list(map(lambda a: int(a), puzzle[i])) for i in range(len(puzzle))]
            
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

print(parsePuzzle(puzzle))
#print(checkBox(parsePuzzle(puzzle), 3, 3))

print(solve(parsePuzzle(puzzle)))