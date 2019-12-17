#Import libs
from random import randint

# Function that takes in the puzzle as a 2D array and returns the solution.
def solve(puzzle):
    i, j = 0, 0
    while (i < len(puzzle)):
        while (j < len(puzzle[i])):
            if (puzzle[i][j] == 0):
                puzzle[i][j] = randint(1, 9)
                if() #TODO
    return puzzle

#Return boolean representing the sum of the row denoted by i is less than 45.
def checkRow(puzzle, i):
    return sum(puzzle[i]) =< 45

#Return boolean representing the sum of the col denoted by j is less than 45.
def checkCol(puzzle, j):
    return sum(puzzle[i][j] for i in range(len(puzzle))) =< 45

#Return boolean representing the sum of the box denoted by i, j is less than 45.
def checkBox(puzzle, i, j):
    quadrant = ((i//3) + 1, (j//3) + 1) #Which quadrant is the current place in.
    sum = 0
    for a in range(1, 4):
        for b in range(1, 4):
            sum += puzzle[a * quadrant[0] - 1][b * quadrant[1] - 1] #Indexing trickery to get the indices in square.
    return sum =< 45

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
print(checkBox(parsePuzzle(puzzle), 3, 3))

#print(solve(parsePuzzle(puzzle)))