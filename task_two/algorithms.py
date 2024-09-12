import random
from collections import deque
from typing import List, Tuple

from helper.tools import print_grid

LAND = 'L'
WATER = 'W'


def generate_grid(m: int, n: int, land_percentage: float) -> List[List[str]]:
    """Generates a grid with specified dimensions and percentage of land."""
    total_cells = m * n
    land_cells = int((land_percentage / 100) * total_cells)

    cells = [LAND] * land_cells + [WATER] * (total_cells - land_cells)
    random.shuffle(cells)

    return [cells[i * n:(i + 1) * n] for i in range(m)]


def find_shortest_path_water_bfs(grid: List[List[str]], start, goal) -> List[Tuple[int, int]]:
    """
    Finds the shortest path between start and goal points using BFS, considering water cells as traversable.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 'W' and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return []


def main() -> None:
    """
    Main function to handle user input and execute the pathfinding algorithm.
    """

    m = int(input("Enter the number of rows (M): "))
    n = int(input("Enter the number of columns (N): "))
    land_percentage = float(input("Enter the percentage of land (0-100): "))

    grid = generate_grid(m, n, land_percentage)
    print("Generated Grid:")
    print_grid(grid)

    start = tuple(map(int, input("Enter the coordinates of point A (row, col): ").split()))
    goal = tuple(map(int, input("Enter the coordinates of point A (row, col): ").split()))

    path = find_shortest_path_water_bfs(grid, start, goal)

    if path:
        print("Shortest path found:")
        print(path)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
