# Set the size of the pattern
n = 5

# Traverse the rows 
for i in range(1, n+1):

    # Traverse the columns in each row
    for j in range(1, n+1):

        # Print stars only if sides of square
        if i==1 or j==1 or i==n or j==n:
            print(" *", end = "")

        # Else print spaces
        else:
            print("  ", end = "")

    # Move to the next line
    print()
