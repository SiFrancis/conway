import random
from os import name, system
from time import sleep

GRID_HEIGHT: int = 20
GRID_WIDTH: int = 20
TIME_LIMIT: int = 1000  # in rounds

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


def makeN_Grid(grid: list[list[int]]):
    n_grid = [[0 for _ in range(GRID_WIDTH)] for __ in range(GRID_HEIGHT)]
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            n_grid[y][x] = sum(list(getNeighbors(x, y).values()))

    return n_grid


def lifeRule(x: int, y: int, n_grid: list[list[int]]):
    # new cell is born if dead cell has 3 living neighbors
    if (grid[y][x] == 0) and (n_grid[y][x] == 3):
        grid[y][x] = 1
    # living cell survives if it has 2-3 living neighbors
    elif grid[y][x] == 1:
        if n_grid[y][x] not in [2, 3]:
            grid[y][x] = 0


def lifeLoop(animate: bool = False):
    t = TIME_LIMIT
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print_grid()
    sleep(1)
    while t > 0:
        if animate:
            if name == "nt":
                _ = system("cls")
            else:
                _ = system("clear")
            print(f"Grid at Turn {TIME_LIMIT - t + 1}:")
            print_grid()
            sleep(0.1)
            if name == "nt":
                _ = system("cls")
            else:
                _ = system("clear")
            t -= 1
        else:
            print(f"Grid at Turn {TIME_LIMIT - t + 1}:")
            print_grid()
            print("\n\n")
            t -= 1

        n_grid = makeN_Grid(grid)
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                lifeRule(x, y, n_grid)


def print_grid():
    # print(f"   {str(list(range(GRID_WIDTH)))[1:-1]}")
    for _, row in enumerate(grid):
        boxes: str = "".join(["󱓻 " if x == 1 else "󱓼 " for x in row])
        print(boxes)


def main():
    print("Hello from conway!")
    for i in range(136):
        setCell(
            random.randrange(2, GRID_WIDTH - 2), random.randrange(2, GRID_HEIGHT - 2), 1
        )
    # setCell(3, 3, 1)
    # setCell(5, 6, 1)
    # setCell(5, 4, 1)
    # setCell(7, 4, 1)
    # setCell(4, 6, 1)
    # setCell(5, 8, 1)
    # setCell(8, 3, 1)
    # setCell(7, 7, 1)
    # print_grid()
    lifeLoop(animate=True)


if __name__ == "__main__":
    main()
