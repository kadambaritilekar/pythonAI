# Practical: Tower of Hanoi using Recursion
#
# Aim:
# To solve the Tower of Hanoi problem using recursion.
#
# Rules:
# 1. Move only one disk at a time.
# 2. Move only the top disk of a rod.
# 3. Never place a larger disk on a smaller disk.
#
# Algorithm:
# 1. If n == 1, move the disk from source to destination.
# 2. Move n-1 disks from source to auxiliary.
# 3. Move the largest disk from source to destination.
# 4. Move n-1 disks from auxiliary to destination.
#
# Time Complexity: O(2^n)
# Space Complexity: O(n), due to the recursion stack.
#
# Advantages:
# 1. Simple and easy to understand.
# 2. Demonstrates recursion.
#
# Disadvantages:
# 1. Requires exponentially many moves.
# 2. Large inputs can cause deep recursion.
#
# Applications:
# Learning recursion and problem decomposition.

def tower_of_hanoi(n, source, auxiliary, destination):

    # Base case: only one disk remains
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: Move the largest disk to destination
    print("Move disk", n, "from", source, "to", destination)

    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main program
n = int(input("Enter the number of disks: "))

if n <= 0:
    print("Please enter a positive number of disks.")
else:
    tower_of_hanoi(n, "A", "B", "C")