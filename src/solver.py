#Import libs
from random import randint

# Function that takes in the puzzle as a 2D array and returns the solution.
def solve(puzzle):
    #stuff
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if (puzzle[i][j] == 0):
                puzzle[i][j] = randint(1, 9)
    return puzzle

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

print(solve(parsePuzzle(puzzle)))