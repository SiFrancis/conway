from itertools import permutations

GRID_HEIGHT: int = 8
GRID_WIDTH: int = 8
TIME_LIMIT: int = 10  # in rounds

grid: list[list[int]] = [[0 for _ in range(GRID_WIDTH)] for __ in range(GRID_HEIGHT)]


def setCell(x: int, y: int, status: int):
    # note: coords start at (0,0) topleft corner
    if x not in range(GRID_WIDTH):
        raise IndexError("x coordinate out of grid bounds")
    elif y not in range(GRID_HEIGHT):
        raise IndexError("y coordinate out of grid bounds")
    elif status not in [0, 1]:
        raise ValueError("cell status must be 0 (dead) or 1 (alive)")
    else:
        grid[y][x] = status


def getNeighbors(x: int, y: int):
    valid_x = [x for x in range(x - 1, x + 2) if x in range(GRID_WIDTH)]
    valid_y = [y for y in range(y - 1, y + 2) if y in range(GRID_HEIGHT)]

    # print(valid_x)
    # print(valid_y)

    poslist = [(x, y) for x in valid_x for y in valid_y]
    poslist.remove((x, y))
    n_dict = {(x, y): grid[y][x] for x, y in poslist}
    return n_dict


def lifeLoop(initGrid: list[list[int]]):
    t = TIME_LIMIT
    while t > 0:
        pass


def print_grid():
    print(f"   {str(list(range(GRID_WIDTH)))[1:-1]}")
    for i, row in enumerate(grid):
        print(f"{i} {row}")


def main():
    print("Hello from conway!")
    # print_grid()
    setCell(4, 3, 1)
    setCell(3, 3, 1)
    setCell(5, 4, 1)
    setCell(2, 1, 1)
    print_grid()
    n = getNeighbors(4, 3)
    print(n)


if __name__ == "__main__":
    main()
