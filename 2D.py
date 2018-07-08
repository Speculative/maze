# Useful constants
UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

ROW = 0
COL = 1

DIRECTION_OFFSET = {
    UP:    (-1,  0),
    DOWN:  ( 1,  0),
    LEFT:  ( 0, -1),
    RIGHT: ( 0,  1),
}

DIRECTION_COMPLEMENT = {
    UP:    DOWN,
    DOWN:  UP,
    LEFT:  RIGHT,
    RIGHT: LEFT,
}

# Utils
def width(grid):
    return len(grid[0])

def height(grid):
    return len(grid)

def pretty_print(grid):
    print('#' * (width(grid) * 2 + 1))
    for row in range(width(grid)):
        line = grid[row]
        if (row != 0):
            print('#' + ''.join(
                ['+-' if has_wall(cell, UP) else '+.' for cell in line]
            )[1:] + '#')
        print('#' + ''.join(
            ['|.' if has_wall(cell, LEFT) else '..' for cell in line]
        )[1:] + '#')
    print('#' * (width(grid) * 2 + 1))

def clone_grid(grid):
    return [list.copy(row) for row in grid]

def in_direction(row, col, direction):
    offset = DIRECTION_OFFSET[direction]
    return (row + offset[ROW], col + offset[COL])

# A 2D maze consists of grid points of the following values:
# (up, down, left, right)
# where each tuple element is a boolean representing a wall in that direction
def generate_grid(row, col):
    return [[(True, True, True, True) for _ in range(row)] for _ in range(col)]

# Add or remove a wall
# The corresponding wall in the adjacent cell will be modified to match unless
# it's at the edge of the grid.
def set_wall(grid, row, col, direction, blocked):
    return safe_modify(clone_grid(grid), row, col, direction, blocked)

def safe_modify(grid, row, col, direction, blocked):
    drow, dcol = in_direction(row, col, direction)
    grid[row][col] = modify_cell(grid[row][col], direction, blocked)
    if not(drow < 0
           or drow > width(grid)
           or dcol < 0
           or dcol > height(grid)):
        grid[drow][dcol] = modify_cell(
            grid[drow][dcol],
            DIRECTION_COMPLEMENT[direction],
            blocked)
    return grid

def modify_cell(cell, direction, blocked):
    return tuple([cell[d] if d != direction else blocked for d in DIRECTIONS])

def has_wall(cell, direction):
    return cell[direction]

grid = generate_grid(4, 4)
grid = set_wall(grid, 0, 0, RIGHT, False)
grid = set_wall(grid, 0, 1, DOWN, False)
grid = set_wall(grid, 1, 1, RIGHT, False)
grid = set_wall(grid, 1, 2, DOWN, False)
grid = set_wall(grid, 2, 2, RIGHT, False)
grid = set_wall(grid, 2, 3, DOWN, False)
pretty_print(grid)
