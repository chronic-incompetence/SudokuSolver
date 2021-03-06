def is_empty(grid, loc):
    '''Function to find an empty space in the grid.

    Args:
        grid (List): The complete Sudoku.
        loc (List): The coordinated of the empty space.

    Returns:
        Bool: True if the space is empty, False if oherwise.
    '''
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                loc[0] = i
                loc[1] = j
                return True
    return False


def in_row(grid, row, column, num):
    '''Function to check whether the number is present in the current row.

    Args:
        grid (List): Thw complete Sudoku.
        row (Integer): The row to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the space is empty, False if oherwise.
    '''
    for i in range(9):
        if grid[row][i] == num and column != i:
            return True
    return False


def in_cloumn(grid, row, column, num):
    '''Function to check whether the number is present in the current column.

    Args:
        grid (List): Thw complete Sudoku.
        col (Integer): The column to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the space is empty, False if oherwise.
    '''
    for i in range(9):
        if grid[i][column] == num and row != i:
            return True
    return False


def in_box(grid, row, column, num):
    '''Function to check whether the number is present in the box.

    Args:
        grid (List): The complete Sudoku.
        row (Integer): The row to be checked.
        column (Integer ): The cloumn to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the space is empty, False if oherwise.
    '''
    for i in range(3):
        for j in range(3):
            if grid[row+i][column+j] == num and row != i and column != j:
                return True
    return False


def is_safe(grid, row, column, num):
    '''Function to call the row, column and box check funtions.

    Args:
        grid (List): The entire Sudoku.
        row (Integer): The row to be checked.
        column (Integer): The column to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True is all the checks return a True value, False if otherwise.
    '''
    return not in_row(grid, row, column, num) and not in_cloumn(grid, row, column, num) and not in_box(grid, row - row % 3, column - column % 3, num)


def solve_puzzle(grid):
    '''Function to solve the given Sudoku.

    Args:
        grid (List): The entire Sudoku.

    Returns:
        Bool: True if the tentative assignment of the number to a cell  is correct, False is otherwise. 
        The boolean is also used to decide whether or not a solution exists for the given Sudoku. 
    '''
    loc = [0, 0]
    if not is_empty(grid, loc):
        return True
    row = loc[0]
    column = loc[1]
    for num in range(1, 10):
        if is_safe(grid, row, column, num):
            grid[row][column] = num
            if solve_puzzle(grid):
                return True
            grid[row][column] = 0
    return False


def print_sudoku(grid):
    '''Fundtion to print the Sudoku grid.

    Args:
        grid (List): The entire Sudoku.
    '''
    for row in grid:
        print(row)


if __name__ == "__main__":
    grid = list()
    for _ in range(9):
        row = list(map(int, input().split()))
        print(row)
        grid.append(row)
    print(grid)
    if solve_puzzle(grid):
        print_sudoku(grid)
    else:
        print('There is no valid solution.')
