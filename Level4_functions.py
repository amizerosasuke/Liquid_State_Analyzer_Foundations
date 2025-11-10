# Global data (available to all functions)
liquids = ["Water", "Mercury", "Ethanol", "Nitrogen", "Oxygen"]
freezing_points = [0, -39, -114, -210, -218]
boiling_points = [100, 357, 78, -196, -183]

# ============================================================================
# PART 12: Simple Functions (No Parameters)
# ============================================================================
print("PART 1: Simple Functions")
print("-" * 50)

# TODO 17: Create a function called 'display_welcome' that prints a welcome message
# Hint:
# def display_welcome():
#     print("Welcome to the Liquid State Analyzer!")
#     print("This program analyzes liquid states based on temperature.")

def display_welcome():
     print("Welcome to the Liquid State Analyzer!")
     print("This program analyzes liquid states based on temperature.")

# TODO 18: Call the display_welcome function
# Hint: Just write the function name with parentheses: display_welcome()

display_welcome()

# Testing Part 12
print("\nCongrats! Part 12 complete — you created and called a function!\n")

# ============================================================================
# PART 13: Functions with Parameters
# ============================================================================
print("PART 2: Functions with Parameters")
print("-" * 50)

# TODO 19: Create a function called 'display_liquid_info' that takes one parameter: index
# The function should print information about the liquid at that index
#
# Hint:
# def display_liquid_info(index):
#     print(f"Liquid: {liquids[index]}")
#     print(f"Freezing Point: {freezing_points[index]}°C")
#     print(f"Boiling Point: {boiling_points[index]}°C")

def display_liquid_info(index):
    print(f"Liquid: {liquids[index]}")
    print(f"Freezing Point: {freezing_points[index]}°C")
    print(f"Boiling Point: {boiling_points[index]}°C")

# TODO 20: Call display_liquid_info for the first liquid (index 0)
print("\nInformation about the first liquid:")

display_liquid_info(0)

# TODO 21: Call display_liquid_info for Mercury (index 1)
print("\nInformation about Mercury:")

display_liquid_info(1)

# Testing Part 13
print("\nCongrats! Part 13 complete — you used function parameters!\n")

# ============================================================================
# PART 14: Functions with Return Values
# ============================================================================
print("PART 3: Functions with Return Values")
print("-" * 50)

# TODO 22: Create a function called 'get_state' that takes 3 parameters:
# temperature, freezing_point, and boiling_point
# The function should return "Solid", "Liquid", or "Gas" based on the temperature
#
# Hint:
# def get_state(temperature, freezing_point, boiling_point):
#     if temperature < freezing_point:
#         return "Solid"
#     elif temperature < boiling_point:
#         return "Liquid"
#     else:
#         return "Gas"

def get_state(temperature, freezing_point, boiling_point):
     if temperature < freezing_point:
        return "Solid"
     elif temperature < boiling_point:
         return "Liquid"
     else:
         return "Gas"

# TODO 23: Test the get_state function
# Call it with temperature=25, freezing_point=0, boiling_point=100
# Store the result in a variable called 'water_state'

water_state = get_state(25, 0, 100)

# Testing Part 14
try:
    print(f"\nWater at 25°C is in the {water_state} state")
    print("Congrats! Part 14 complete — you used return values!\n")
except NameError as e:
    print("Oops! You need to complete TODO 22-23 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 15: Functions that Call Other Functions
# ============================================================================
print("PART 4: Functions Calling Functions")
print("-" * 50)

# TODO 24: Create a function called 'analyze_liquid' that takes 2 parameters:
# liquid_index and temperature
# This function should:
# 1. Get the liquid name, freezing point, and boiling point using the index
# 2. Call the get_state function to determine the state
# 3. Print a complete analysis
# 4. Return the state
#
# Hint:
# def analyze_liquid(liquid_index, temperature):
#     liquid_name = liquids[liquid_index]
#     freezing = freezing_points[liquid_index]
#     boiling = boiling_points[liquid_index]
#
#     state = get_state(temperature, freezing, boiling)
#
#     print(f"\n🔬 ANALYSIS RESULTS:")
#     print(f"Liquid: {liquid_name}")
#     print(f"Temperature: {temperature}°C")
#     print(f"State: {state}")
#
#     return state

def analyze_liquid(liquid_index, temperature):
     liquid_name = liquids[liquid_index]
     freezing = freezing_points[liquid_index]
     boiling = boiling_points[liquid_index]

     state = get_state(temperature, freezing, boiling)

     print(f"\n🔬 ANALYSIS RESULTS:")
     print(f"Liquid: {liquid_name}")
     print(f"Temperature: {temperature}°C")
     print(f"State: {state}")

     return state

# TODO 25: Test the analyze_liquid function
# Analyze Water (index 0) at -10°C
print("\nTest 1:")

analyze_liquid (0,-10)

# TODO 26: Analyze Nitrogen (index 3) at -200°C
print("\nTest 2:")

analyze_liquid(3,-200)

# Testing Part 15
print("\nCongrats! Part 15 complete — functions can call other functions!\n")

# ============================================================================
# PART 16: Input Validation Function
# ============================================================================
print("PART 5: Input Validation with Functions")
print("-" * 50)

# TODO 27: Create a function called 'get_valid_choice' that takes no parameters
# This function should:
# 1. Display all available liquids with numbers
# 2. Use a while loop to get a valid choice (1-5)
# 3. Return the choice as an integer
#
# Hint:
# def get_valid_choice():
#     print("\nAvailable liquids:")
#     for i in range(len(liquids)):
#         print(f"{i+1}. {liquids[i]}")
#
#     choice = 0
#     while choice < 1 or choice > 5:
#         choice = int(input("\nSelect a liquid (1-5): "))
#         if choice < 1 or choice > 5:
#             print("Invalid! Please enter 1-5.")
#
#     return choice

def get_valid_choice():
     print("\nAvailable liquids:")
     for i in range(len(liquids)):
         print(f"{i+1}. {liquids[i]}")

     choice = 0
     while choice < 1 or choice > 5:
         choice = int(input("\nSelect a liquid (1-5): "))
         if choice < 1 or choice > 5:
             print("Invalid! Please enter 1-5.")

     return choice
# Testing Part 16
print("\nCongrats! Part 16 complete — you created a validation function!\n")

# ============================================================================
# PART 17: Main Program Function
# ============================================================================
print("PART 6: Putting It All Together")
print("-" * 50)

# TODO 28: Create a function called 'run_analyzer' that:
# 1. Calls display_welcome()
# 2. Calls get_valid_choice() and stores the result
# 3. Asks for a temperature
# 4. Calls analyze_liquid() with the choice and temperature
# 5. Prints a goodbye message
#
# Hint:
# def run_analyzer():
#     display_welcome()
#
#     choice = get_valid_choice()
#     liquid_index = choice - 1  # Convert to 0-based index
#
#     temperature = float(input("\nEnter temperature in Celsius: "))
#
#     state = analyze_liquid(liquid_index, temperature)
#
#     print("\n" + "=" * 50)
#     print("Thank you for using the Liquid State Analyzer!")
#     print("=" * 50)

def run_analyzer():
     display_welcome()

     choice = get_valid_choice()
     liquid_index = choice - 1  # Convert to 0-based index

     temperature = float(input("\nEnter temperature in Celsius: "))

     state = analyze_liquid(liquid_index, temperature)

     print("\n" + "=" * 50)
     print("Thank you for using the Liquid State Analyzer!")
     print("=" * 50)

# TODO 29: Call the run_analyzer function to start the program

run_analyzer()

# ============================================================================
# CONGRATULATIONS!
# ============================================================================
print("\n" + "=" * 50)
print("LEVEL 4 COMPLETE!")
print("=" * 50)
print("\nYou've learned:")
print("How to define functions with def")
print("How to use parameters (inputs)")
print("How to use return values (outputs)")
print("How to organize code with functions")
print("How functions can call other functions")
print("=" * 50)