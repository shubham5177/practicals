import heapq

# Initial and goal puzzle (0 = blank)
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Count misplaced tiles
def h(s):
    return sum(s[i] != goal[i] and s[i] != 0 for i in range(9))

# Display puzzle in grid format
def show(s):
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print()

# Create priority queue
q = [(h(start), 0, start)]
visited = {start}

# Run A* search
while q:
    f, g, s = heapq.heappop(q)

    # Display current puzzle
    show(s)

    # Check goal
    if s == goal:
        print("Goal reached in", g, "moves!")
        break

    # Find blank position
    z = s.index(0)
    r, c = z // 3, z % 3

    # Try four directions
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc

            # Swap blank with adjacent tile
            new = list(s)
            new[z], new[nz] = new[nz], new[z]
            new = tuple(new)

            if new not in visited:
                visited.add(new)
                heapq.heappush(q, (g + 1 + h(new), g + 1, new))
                