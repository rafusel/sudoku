'''
UTILITY FUNCTIONS USED AT VARIOUS STAGES IN DEBUGGING
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