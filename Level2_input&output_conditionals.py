# ============================================================================
# PART 3: Input and Output
# ============================================================================
print("PART 3: Input and Output")
print("-" * 50)

# TODO 7: Ask the user for their favorite liquid using input()
# Store the answer in a variable called 'favorite_liquid'
# Hint: favorite_liquid = input("What is your favorite liquid? ")
favorite_liquid = input("what's your favourite liquid")

# TODO 8: Ask the user to enter a temperature (as a number)
# Store it in a variable called 'temperature'
# IMPORTANT: Convert the input to float using float()
# Hint: temperature = float(input("Enter temperature in Celsius: "))

temperature = float(input("Enter temperature in Celsius"))

boiling_point = float(input("Enter the boiling point of your favorite liquid"))

freezing_point = float(input("Enter the freezing point of your favourite liquid"))
# Testing Part 3 - do not modify!
print("\nTesting Part 3...")
try:
    print("\nYou entered:")
    print("Favorite liquid: " + favorite_liquid)
    print("Temperature: " + str(temperature) + "°C")
    print(
        "Congrats! You passed Part 3 — awesome job. Keep exploring and try different inputs!\n"
    )
except NameError as e:
    print("Oops! Looks like you missed TODO 7-8.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 4: Basic Operations
# ============================================================================
print("PART 4: Basic Operations")
print("-" * 50)

# TODO 9: Calculate the temperature range (boiling_point - freezing_point)
# Store the result in a variable called 'temperature_range'
temperature_range = (boiling_point - freezing_point)
liquid_name = favorite_liquid
# TODO 10: Calculate how far the current temperature is from freezing
# Store the result in a variable called 'degrees_from_freezing'
# Hint: Use temperature - freezing_point

degrees_from_freezing = (temperature - freezing_point)

# Testing Part 4 - do not modify!
print("\nTesting Part 4...")
try:
    print("Temperature range for water: " + str(temperature_range) + "°C")
    print("Current temperature is " + str(degrees_from_freezing) + "°C from freezing")
    print(
        "Congrats! You passed Part 4 — math master in the making. Try different temperatures to practice!\n"
    )
except NameError as e:
    print("Oops! You need to complete TODO 9-10 to finish this part.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 5: Conditional Statements
# ============================================================================
print("PART 5: Conditional Statements")
print("-" * 50)

print(f"\nAnalyzing {liquid_name} at {temperature}°C...")

# TODO 11: Write an if/elif/else statement to determine the state
# If temperature is less than freezing_point, the state is "Solid"
# Else if temperature is less than boiling_point, the state is "Liquid"
# Else, the state is "Gas"
# Store the result in a variable called 'state'


if temperature < freezing_point:
    state = "Solid"
elif temperature < boiling_point:
    state = "Liquid"
else:
    state = "Gas"



# Hint: Structure should be:
# if temperature < freezing_point:
#     state = "Solid"
# elif temperature < boiling_point:
#     state = "Liquid"
# else:
#     state = "Gas"




# Testing Part 5 - do not modify!
print("\nTesting Part 5...")
try:
    print(f"\nRESULT: At {temperature}°C, {liquid_name} is in the {state} state!")

    # Additional analysis
    if state == "Solid":
        print(f"It needs to warm up {freezing_point - temperature}°C to melt.")
    elif state == "Liquid":
        print(f"It's {temperature - freezing_point}°C above freezing.")
        print(f"It's {boiling_point - temperature}°C below boiling.")
    else:
        print(f"It's {temperature - boiling_point}°C above boiling!")

    # Friendly grade-8 style success message
    print(
        "\nEpic! You passed Part 5 — conditionals conquered. Great work! Keep experimenting and have fun coding."
    )
except NameError as e:
    print("Oops! You need to complete TODO 11 to analyze the state.")
    print(f"Error: {e}\n")
    exit()


# ============================================================================
# CONGRATULATIONS!
# ============================================================================
print("=" * 50)
print("LEVEL 2 COMPLETE!")
print("=" * 50)
print("\nYou've learned:")
print("How to get input from users")
print("How to do basic math operations")
print("How to make decisions with if/elif/else")
print("=" * 50)
