# Define the grid (0 = free, 1 = obstacle)
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]

# Set starting position and goal
agent = [0, 0]
goal = [2, 2]

# Store the internal state
memory = []

# Move until the goal is reached
while agent != goal:

    # Remember current position
    memory.append(agent.copy())

    # Get current row and column
    r, c = agent

    # Move down if possible
    if r + 1 < 3 and grid[r + 1][c] == 0:
        agent = [r + 1, c]

    # Otherwise, move right if possible
    elif c + 1 < 3 and grid[r][c + 1] == 0:
        agent = [r, c + 1]

    # Otherwise, stop
    else:
        print("Path blocked!")
        break

# Display results
print("Final Position:", agent)
print("Goal Position:", goal)
print("Agent Memory:", memory)

# Check the result
if agent == goal:
    print("Goal reached!")