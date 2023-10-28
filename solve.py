from generate_puzzle import generate
import numpy as np
import pandas as pd

from functools import wraps
from time import time


# timer wrapper from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
def timing(f):
    @wraps(f)
    def wrap(*args):
        ts = time()
        result = f(*args)
        te = time()
        
        arr = np.array(args[0])
        arr = pd.DataFrame(arr)
        arr.columns = ['']*arr.shape[1]
        
        print('----------------------------')
        print('%r' % arr)
        print('\ntook: %2.4f sec' % (te-ts))
        
        return result
    return wrap


def _row_check(row: np.ndarray, val: int):
    """Helper function to check the specific row

    Args:
        row (np.ndarray): the row to check
        val (int): the value to check

    Returns:
        bool: is the value valid in that spot
    """
    if val in row:
        return False
    return True


def _col_check(col: np.ndarray, val: int):
    """Helper function to check the specific column

    Args:
        col (np.ndarray): the column to check
        val (int): the value to check

    Returns:
        bool: is the value valid in that spot
    """
    if val in col:
        return False
    return True
    


def _box_check(box: np.ndarray, val: int):
    """Helper function to check the specific box

    Args:
        box (np.ndarray): the box to check
        val (int): the value to check

    Returns:
        bool: is the value valid in that spot
    """
    if val in box:
        return False
    return True


def _valid(grid: np.ndarray, val: int, cell: tuple):
    """Check if a value is valid to put in a specific cell

    Args:
        grid (np.ndarray): _description_
        val (int): _description_
        cell (tuple): _description_

    Returns:
        bool: whether the value is valid to put in that specific cell
    """
    row = grid[cell[0]]
    if not _row_check(row, val):
        return False
    
    col = grid.T[cell[1]]
    if not _col_check(col, val):
        return False
    
    x = cell[0]//3*3
    y = cell[1]//3*3
    box = grid[x: x + 3, y: y + 3]
    if not _box_check(box, val):
        return False
        
    return True

@timing
def solve(grid: np.ndarray):
    """Solve the sudoku using backtracking

    Args:
        grid (np.ndarray): the uncompleted puzzle to solve

    Returns:
        np.ndarray: the solved puzzle
    """
    if 0 not in grid:
        return True
    
    unfilled = list(zip(*np.where(grid == 0)))[0]
    
    for num in range(1, 10):
        if _valid(grid, num, unfilled):
            grid[unfilled] = num

            if solve(grid):
                return True

            grid[unfilled] = 0
            
    return False


if __name__ == "__main__":
    
    sudoku = generate()
    solve(sudoku)