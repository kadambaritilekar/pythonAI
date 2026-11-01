# Number-Guessing Agent using Binary Search

# Set the range of possible numbers
low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    # Find the middle number
    guess = (low + high) // 2

    print(f"My guess is: {guess}")
    feedback = input("Enter 'low', 'high', or 'correct': ").lower()

    if feedback == "correct":
        print("Yay! I guessed the number!")
        break

    elif feedback == "low":
        # The secret number is greater than the guess
        low = guess + 1

    elif feedback == "high":
        # The secret number is smaller than the guess
        high = guess - 1

    else:
        print("Invalid input! Please enter low, high, or correct.")

else:
    print("Your feedback was inconsistent, or no number remains.")

# --------------------------------------------------
# 1. TIME AND SPACE COMPLEXITY
# Time Complexity: O(log n), because the search range
# is reduced by half after each valid guess.
# Space Complexity: O(1), because only a few variables
# are used, regardless of the range size.

# 2. WHY IT WORKS
# Binary search checks the middle number and uses
# feedback to eliminate half of the remaining range.
# It continues until the correct number is found
# or no possible numbers remain.

# 3. PSEUDOCODE
# START
# Set low = 1 and high = 100
# WHILE low <= high:
#     guess = (low + high) // 2
#     Get feedback from the user
#     IF feedback is correct:
#         Display success and STOP
#     ELSE IF feedback is low:
#         low = guess + 1
#     ELSE IF feedback is high:
#         high = guess - 1
#     ELSE:
#         Display invalid input
# Display failure if the search range becomes empty
# END

# 4. ALGORITHM
# Step 1: Initialize the range from 1 to 100.
# Step 2: Calculate the middle number.
# Step 3: Ask the user whether the guess is low, high,
#         or correct.
# Step 4: Update the range according to the feedback.
# Step 5: Repeat until the number is guessed or the
#         range becomes empty.