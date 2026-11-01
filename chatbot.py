# Practical 2: Simple Chatbot using Python

# Display a welcome message
print("Chatbot: Hello! Welcome to the Simple Chatbot.")
print("Chatbot: You can ask me simple questions.")
print("Chatbot: Type 'bye' to end the conversation.")

while True:
    # Get input from the user and convert it to lowercase
    user_input = input("You: ").lower().strip()

    # Check the user's input and provide a suitable response
    if user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Chatbot: I am a simple rule-based chatbot.")

    elif "how are you" in user_input:
        print("Chatbot: I am doing well! How about you?")

    elif "artificial intelligence" in user_input or user_input == "ai":
        print("Chatbot: AI enables machines to perform tasks that usually require human intelligence.")

    elif "thank" in user_input:
        print("Chatbot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        # Default response for unrecognized input
        print("Chatbot: Sorry, I didn't understand that. Please try asking something else.")

# --------------------------------------------------
# 1. TIME AND SPACE COMPLEXITY
# Time Complexity: O(1) per message, because the
# program checks a fixed number of conditions.
# Space Complexity: O(1) auxiliary space, because
# it stores only a few variables and fixed rules.
# These complexities assume the rules remain fixed
# and input length is bounded.

# 2. WHY THIS CODE WORKS
# The chatbot receives a message, converts it to
# lowercase, and checks it against predefined rules.
# It prints the matching response. If no rule matches,
# it displays a default response.
# The loop continues until the user types 'bye',
# 'exit', or 'quit'.

# 3. IS THERE A BETTER OPTION?
# For a basic practical, this rule-based chatbot is
# simple and easy to understand.
# For larger chatbots, storing rules in a dictionary
# or using NLP can improve flexibility.
# Advanced AI chatbots can understand more varied
# inputs, but they require additional techniques.

# 4. PSEUDOCODE
# START
# Display welcome message
# REPEAT:
#     Read user input
#     Convert input to lowercase
#     IF input matches a greeting:
#         Display greeting response
#     ELSE IF input asks the bot's name:
#         Display name response
#     ELSE IF input asks how the bot is:
#         Display status response
#     ELSE IF input asks about AI:
#         Display AI explanation
#     ELSE IF input expresses thanks:
#         Display a polite response
#     ELSE IF input is 'bye', 'exit', or 'quit':
#         Display goodbye message
#         STOP
#     ELSE:
#         Display default response
# END REPEAT

# 5. ALGORITHM
# Step 1: Display a welcome message.
# Step 2: Accept a message from the user.
# Step 3: Convert the message to lowercase.
# Step 4: Match the message against predefined rules.
# Step 5: Display the corresponding response.
# Step 6: If the input is an exit command, stop.
# Step 7: Otherwise, repeat from Step 2.