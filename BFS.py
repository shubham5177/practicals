
from collections import deque

# Grid: 0 = free cell, 1 = obstacle
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]

# Starting and goal positions
start = (0, 0)
goal = (2, 2)

# Queue stores positions and their paths
queue = deque([(start, [start])])

# Store visited positions
visited = {start}

# BFS algorithm
while queue:
    position, path = queue.popleft()

    # Check if goal is reached
    if position == goal:
        print("Path found:", path)
        print("Steps:", len(path) - 1)
        break

    r, c = position

    # Move down, up, right, and left
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        next_pos = (nr, nc)

        # Check boundaries and obstacles
        if (0 <= nr < 3 and 0 <= nc < 3
                and grid[nr][nc] == 0
                and next_pos not in visited):

            # Mark position as visited
            visited.add(next_pos)

            # Add new position and path to queue
            queue.append((next_pos, path + [next_pos]))

else:
    print("No path found!")
