import copy
import sys
import json
import math

class SudokuSolver:
    #initiate Puzzle in our class
    def __init__(self, puzzle):
        n = len(puzzle)
        #check for valid dimensions (Even height, width, can make mini boxes)
        if (n <= 0 or (n ** 2 != math.floor(n ** 2))):
            print("ERROR: invalid sudoku input")
            sys.exit(1)
        for i in range(n):
            if len(puzzle[i]) != n:
                print("ERROR: invalid sudoku input")
                sys.exit(1)
        self.size = n
        self.puzzle = puzzle
        self.box_size = int(self.size ** 0.5)

    def solve(self):
        #outsource our solve to recursive backtrack
        works = self.recursive_backtracking(self.puzzle)
        if (works):
            print("Here is the finished puzzle:")
            self.print_puzzle()
        return
    
    def recursive_backtracking(self, puzzle):
        if self.check_finished(puzzle):
            return True
        for i in range(self.size):
            for j in range(self.size):
                if puzzle[i][j] == 0:
                    #here we implement forward checking, with arc consistency
                    #we treat the col, row, block relationship as arcs
                    #and return values that satisfy the 'arcs'
                    for k in self.get_allowed_values(puzzle, i, j):
                        puzzle[i][j] = k
                        if self.recursive_backtracking(puzzle):
                            return True
                    puzzle[i][j] = 0
                    return False
        return False

    def get_allowed_values(self, puzzle, row, col):
        values = set(range(1, self.size + 1))
        for i in range(self.size):
            values.discard(puzzle[row][i])  # Remove values in the same row
            values.discard(puzzle[i][col])  # Remove values in the same column
        start_row, start_col = (row // self.box_size) * self.box_size, (col // self.box_size) * self.box_size
        for i in range(self.box_size):
            for j in range(self.box_size):
                values.discard(puzzle[start_row + i][start_col + j])  # Remove values in the same box
        return list(values)

    #Since we forward check, we only need to see if it's filled out
    def check_finished(self, puzzle):
        for i in range(self.size):
            for j in range(self.size):
                if puzzle[i][j] == 0:
                    return False
        return True

    #wanted to show what different code without forward checking would need.
    #This was initially built using these functions, before forward checking was
    #implemented.

    # def check_finished(self, puzzle):
    #     for i in range(self.size):
    #         row = []
    #         col = []  # Initialize separate arrays for each row and column
    #         for j in range(self.size):
    #             if puzzle[i][j] == 0 or puzzle[i][j] in row:
    #                 return False
    #             if puzzle[j][i] in col:  # Check for duplicates in columns
    #                 return False
    #             if puzzle[i][j] != 0:
    #                 row.append(puzzle[i][j])
    #             if puzzle[j][i] != 0:
    #                 col.append(puzzle[j][i])
    #     for i in range(self.size):
    #         col = []
    #         for j in range(self.size):
    #             if puzzle[j][i] in col:
    #                 return False
    #             col.append(puzzle[j][i])
    #     for i in range(self.box_size):
    #         for j in range(self.box_size):
    #             box = []
    #             for k in range(self.box_size):
    #                 for l in range(self.box_size):
    #                     if puzzle[(i * self.box_size)+k][(j * self.box_size)+l] in box:
    #                         return False
    #                     box.append(puzzle[(i * self.box_size)+k][(j * self.box_size)+l])
    #     return True
            
    # def check_constraints(self, puzzle):
    #     for i in range(self.size):
    #         row = []
    #         col = []  # Initialize separate arrays for each row and column
    #         for j in range(self.size):
    #             if puzzle[i][j] in row:
    #                 return False
    #             if puzzle[j][i] in col:  # Check for duplicates in columns
    #                 return False
    #             if puzzle[i][j] != 0:
    #                 row.append(puzzle[i][j])
    #             if puzzle[j][i] != 0:
    #                 col.append(puzzle[j][i])
    #     for i in range(self.box_size):
    #         for j in range(self.box_size):
    #             box = []
    #             for k in range(self.box_size):
    #                 for l in range(self.box_size):
    #                     if puzzle[(i * self.box_size)+k][(j * self.box_size)+l] in box:
    #                         return False
    #                     if puzzle[(i * self.box_size)+k][(j * self.box_size)+l] != 0:
    #                         box.append(puzzle[(i * self.box_size)+k][(j * self.box_size)+l])
    #     return True

    def print_puzzle(self):
        for row in self.puzzle:
            print(row)
        return

                
if __name__ == "__main__":
    # Example Sudoku puzzle

    print("Welcome to the Sudoku Solver! Do you want to input a custom puzzle or me to solve the 2 HW examples")
    custom = input("Custom Puzzle? (y for yes, anything else for no): ")

    if custom == "Y" or custom =="y":
        print("\nEnter your Custom Puzzle as a string representation of an array of arrays.\n"
        "The empty values should be 0. Please print as one line, or copy and paste as one line")
        print("\nExample: \n[[6, 0, 8, 7, 0, 2, 1, 0, 0],\n"
            "[4, 0, 0, 0, 1, 0, 0, 0, 2],\n" 
            "[0, 2, 5, 4, 0, 0, 0, 0, 0],\n"
            "[7, 0, 1, 0, 8, 0, 4, 0, 5],\n"
            "[0, 8, 0, 0, 0, 0, 0, 7, 0],\n"
            "[5, 0, 9, 0, 6, 0, 3, 0, 1],\n" 
            "[0, 0, 0, 0, 0, 6, 7, 5, 0],\n" 
            "[2, 0, 0, 0, 9, 0, 0, 0, 8],\n" 
            "[0, 0, 6, 8, 0, 5, 2, 0, 3]]\n"
            "\n On Terminal: [[6, 0, 8, 7, 0, 2, 1, 0, 0],"
            "[4, 0, 0, 0, 1, 0, 0, 0, 2],[0, 2, 5, 4, 0, 0, 0, 0, 0],"
            "[7, 0, 1, 0, 8, 0, 4, 0, 5],[0, 8, 0, 0, 0, 0, 0, 7, 0],"
            "[5, 0, 9, 0, 6, 0, 3, 0, 1],[0, 0, 0, 0, 0, 6, 7, 5, 0],"
            "[2, 0, 0, 0, 9, 0, 0, 0, 8],[0, 0, 6, 8, 0, 5, 2, 0, 3]]")
        try:
            puzzle = json.loads(input("\nEnter Puzzle:\n"))
            solver = SudokuSolver(puzzle)
            print("Your Puzzle:")
            solver.print_puzzle()
            solver.solve()
            print()
        except:
            print("ERROR: invalid sudoku input")
            sys.exit(1)

        
    else:
        # If no inputted Custom Sudoku, it will do the two hw sudokus
        puzzle = [
            [6, 0, 8, 7, 0, 2, 1, 0, 0],
            [4, 0, 0, 0, 1, 0, 0, 0, 2],
            [0, 2, 5, 4, 0, 0, 0, 0, 0],
            [7, 0, 1, 0, 8, 0, 4, 0, 5],
            [0, 8, 0, 0, 0, 0, 0, 7, 0],
            [5, 0, 9, 0, 6, 0, 3, 0, 1],
            [0, 0, 0, 0, 0, 6, 7, 5, 0],
            [2, 0, 0, 0, 9, 0, 0, 0, 8],
            [0, 0, 6, 8, 0, 5, 2, 0, 3]
        ]
        solver = SudokuSolver(puzzle)
        print("Example #1:")
        solver.print_puzzle()
        solver.solve()
        print()
        puzzle = [
            [0, 7, 0, 0, 4, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 8, 6, 1, 0],
            [3, 9, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 4, 0, 0, 9],
            [0, 0, 3, 0, 0, 0, 7, 0, 0],
            [5, 0, 0, 1, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 7, 6],
            [0, 5, 4, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 1, 0, 0, 5, 0]
        ]
        solver = SudokuSolver(puzzle)
        print("Example #2:")
        solver.print_puzzle()
        solver.solve()
