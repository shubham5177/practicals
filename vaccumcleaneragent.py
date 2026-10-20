# Take input from user
A = input("Room A (Dirty/Clean): ")
B = input("Room B (Dirty/Clean): ")
pos = input("Vacuum position (A/B): ")

# Run the agent
while A == "Dirty" or B == "Dirty":

    # If current room is dirty, clean it
    if pos == "A":
        if A == "Dirty":
            print("Suck: Cleaning Room A")
            A = "Clean"
        else:
            print("Move to Room B")
            pos = "B"

    else:
        if B == "Dirty":
            print("Suck: Cleaning Room B")
            B = "Clean"
        else:
            print("Move to Room A")
            pos = "A"

# Show final result
print("Room A:", A)
print("Room B:", B)
print("All rooms are clean!")