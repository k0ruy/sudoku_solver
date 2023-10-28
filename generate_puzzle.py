import numpy


def _pattern(b: int, r: int,c: int):
    """Generate a valid pattern

    Args:
        b (int): base
        r (int): rows
        c (int): columns

    Returns:
        int: a number for a valid pattern
    """
    
    side = b**2
    return (b*(r%b)+r//b+c)%side


def _shuffle(s: int):
    """Randomize rows, columns and numbers

    Args:
        s (list): the population to shuffle

    Returns:
        list: the shuffled population
    """
    
    from random import sample
    
    return sample(s, len(s)) 


def generate(base: int = 3):
    """Generate the puzzle to solve

    Args:
        base (int): in which base should the puzzle be generated (e.g. 3 for a 9x9 sudoku)
    """
    
    rBase = range(base)
    rows  = [g*base + r for g in _shuffle(rBase) for r in _shuffle(rBase)]
    cols  = [g*base + c for g in _shuffle(rBase) for c in _shuffle(rBase)]
    nums  = _shuffle(range(1, base**2 + 1))

    # produce board using randomized baseline pattern
    board = numpy.array([[nums[_pattern(base, r, c)] for c in cols] for r in rows])
    return board


generate()
    

    