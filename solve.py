from generate_puzzle import generate
import numpy as np


sudoku = generate()


def row_check(row, val):
    if val in row:
        return False
    return True


def col_check(col, val):
    if val in col:
        return False
    return True
    


def box_check(box, val):
    if val in box:
        return False
    return True


def valid(grid: np.ndarray, val: int, cell: tuple):
    row = grid[cell[0]]
    if not row_check(row, val):
        return False
    
    col = grid.T[cell[1]]
    if not col_check(col, val):
        return False
    
    x = cell[0]//3*3
    y = cell[1]//3*3
    box = grid[x: x + 3, y: y + 3]
    if not box_check(box, val):
        return False
        
    return True


def solve(grid):
    if 0 not in grid:
        return True
    
    unfilled = list(zip(*np.where(grid == 0)))[0]
    
    # print(grid[unfilled[0]])
    # return
    for num in range(1, 10):
        if valid(grid, num, unfilled):
            grid[unfilled] = num

            if solve(grid):
                return True

            grid[unfilled] = 0
            
    return False


# def print_board(bo):
#     for i in range(len(bo)):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - - - ")

#         for j in range(len(bo[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")

#             if j == 8:
#                 print(bo[i][j])
#             else:
#                 print(str(bo[i][j]) + " ", end="")

                
if __name__ == "__main__":

    print(sudoku)
    solve(sudoku)
    print("-----------------------------")
    print(sudoku)