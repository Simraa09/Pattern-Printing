# Set the size of the pattern
n = 5

# Printing top half
# Traverse the rows 
for i in range(1, n+1):

    # Print spaces 
    for j in range(1, n-i +1):
        print("  ", end="")

    # Print the stars
    for j in range(1, 2*i):
        print(" *", end = "")
        
    # Move to the next line
    print()


# Printing bottom half
# Traverse the rows 
for i in range(n-1, 0, -1):

    # Print spaces 
    for j in range(1, n-i +1):
        print("  ", end="")

    # Print the stars
    for j in range(1, 2*i):
        print(" *", end = "")
        
    # Move to the next line
    print()