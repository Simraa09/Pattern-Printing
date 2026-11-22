# Set the size of the pattern
n = 5

# Traverse the rows 
for i in range(1, n+1):

    # Traverse the columns in each row
    for j in range(1, i+1):

        # Print the stars in the same line
        print(f" {j}", end = "")
        
    # Move to the next line
    print()