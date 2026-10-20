# Function to solve Tower of Hanoi
def hanoi(n, source, auxiliary, destination):

    # Base condition
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Move n-1 disks to auxiliary rod
    hanoi(n - 1, source, destination, auxiliary)

    # Move largest disk to destination
    print("Move disk", n, "from", source, "to", destination)

    # Move remaining disks to destination
    hanoi(n - 1, auxiliary, source, destination)


# Take number of disks from user
n = int(input("Enter number of disks: "))

# Start the solution
hanoi(n, 'A', 'B', 'C')