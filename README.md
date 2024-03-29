# SUDOKU PROBLEM INTRO
    - Given a sudoku puzzle that is unfinished, complete the puzzle
    - So, given:
    [6, 0, 8, 7, 0, 2, 1, 0, 0]
    [4, 0, 0, 0, 1, 0, 0, 0, 2]
    [0, 2, 5, 4, 0, 0, 0, 0, 0]
    [7, 0, 1, 0, 8, 0, 4, 0, 5]
    [0, 8, 0, 0, 0, 0, 0, 7, 0]
    [5, 0, 9, 0, 6, 0, 3, 0, 1]
    [0, 0, 0, 0, 0, 6, 7, 5, 0]
    [2, 0, 0, 0, 9, 0, 0, 0, 8]
    [0, 0, 6, 8, 0, 5, 2, 0, 3]
    The 0s must be replaced with numbers that satisfy our sudoku.

## REPRESENTING AS A CONSTRAINT SATISFACTION PROBLEM
    - To define our problem as a CSP problem, we need to define
    our variables, domains, and constraints
    - Our variables will be all the empty spaces in the sudoku puzzle
    - The domains for each will be discrete and finite. They will be values
    1 through n, where n is the size of the puzzle given (9 for hw)
    - Our constraints are all hard constraints:
        - Each row must have all unique values
        - Each col must have all unique values
        - Each mini box of sqrt n sizze must have all unique values

## ALGORITHMS & PRUNING:
    - Our satisfaction algorithm implements chronological backtracking search.
    It is an improved version uninformed searching algorithm based on the Depth-first 
    search. Each step considers only one assignment at a time. It also checks
    constraints as the search continues. Consider only new assignments that do
    not conflict with previous ones (incremental goal test).

    - We improve our backtrack search by pruning domains when we recurse and 
    traverse through:
        - We implement forward checking with arc consistency
        - We treat the col, row, block relationship as arcs
        and return values that satisfy the 'arcs'
        - So, we avoid assigning bad values, and instead backtrack
        if there's no possible assignments.
        - This saves times and there will be less recurses

## ASSUMPTIONS:
    - Sudoku is formatted as a list of lists
    - Assumes empty values are 0s
    - Assumes puzzle is solvable with given input

## Notes:
    - It properly solves the HW puzzles, just don't say yes to custom puzzles
    to see the HW problems
    - Custom puzzle can be any size
    - You must do more work as a user to format the custom puzzles for one line input 
    if you want to try using a custom puzzle of any size


