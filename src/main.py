from solver import fullSolve
from generator import generatePuzzle
from misc import *

def main():
    printPuzzle(generatePuzzle())
    print()
    printPuzzle(fullSolve(parsePuzzle(puzzle)))

main()



