# Author: Nicholas Ngobi
# This program generates staircases from 1 to N
def staircase(n):
    # Loop through each stair
    for i in range(1, n+1):
        # Print spaces to align the '#' character
        print(" " * (n-i) + "#" * i)  # Concatenate "#" with "*i" to create the stair pattern

def main():
    # Prompt the user to input the number of stairs and convert it to an integer
    n = int(input("How many stairs do you want to generate?\n"))
    # Call the staircase function to generate the stairs
    staircase(n)

# Entry point of the program
main()