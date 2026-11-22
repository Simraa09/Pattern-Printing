# Set the size of the pattern
n = 5

# Printing the upper half
# Traverse the rows 
for i in range(1, n+1):

    # Print stars on the left side
    for j in range(1, i + 1):
        print(" *", end="")

    # Print spaces
    for j in range(1, 2*(n-i)+1):
        print("  ", end="")

    # Print stars on the right side
    for j in range(1, i + 1):
        print(" *", end="")

    # Move to the next line
    print()


# Printing the bottom half
# Traverse the rows 
for i in range(n-1, 0, -1):

    # Print stars on the left side
    for j in range(1, i + 1):
        print(" *", end="")

    # Print spaces in the middle
    for j in range(1, 2*(n-i)+1):
        print("  ", end="")

    # Print stars on the right side
    for j in range(1, i + 1):
        print(" *", end="")

    # Move to the next line
    print()
