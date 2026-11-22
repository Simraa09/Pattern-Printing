# Set the size of the pattern
n = 5

# Traverse the rows 
for i in range(n, 0, -1):

    # Print spaces 
    for j in range(1, n-i +1):
        print("  ", end="")

    # Print the stars
    for j in range(1, 2*i):
        print(" *", end = "")
        
    # Move to the next line
    print()