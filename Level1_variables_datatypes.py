"""
INSTRUCTIONS:
Complete each TODO section below. Run the program after each level
to test your code. The program will tell you if you're on the right track!
"""

# ============================================================================
# PART 1: Creating Variables
# ============================================================================
print("PART 1: Creating Variables")
print("-" * 50)

# TODO 1: Create a variable called 'liquid_name' and set it to "Water"
# Hint: Use the = sign to assign a value to a variable
# Example: my_variable = "some value"
# Write your code here:

liquid_name= "Water"

# TODO 2: Create a variable called 'freezing_point' and set it to 0
# Hint: This is a number (integer), so don't use quotes
# Write your code here:
freezing_point = 0
# TODO 3: Create a variable called 'boiling_point' and set it to 100.0
# Hint: This is a decimal number (float), notice the .0
# Write your code here:

boiling_point = 100.0

# Testing Part 1 - do not modify!
print("\nTesting Part 1...")
try:
    print(f"Liquid: {liquid_name}")
    print(f"Freezing point: {freezing_point}°C")
    print(f"Boiling point: {boiling_point}°C")
    print("Congrats! You nailed Part 1! Great job creating variables!\n")
except NameError as e:
    print("Oops! Looks like you missed something in Part 1.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 2: Understanding Data Types
# ============================================================================
print("PART 2: Understanding Data Types")
print("-" * 50)

# TODO 4: Create a variable 'student_name' with YOUR name as a string
student_name="tresor"
# TODO 5: Create a variable 'current_grade' and set it to 8 (your grade)(integer)
current_grade= 8

# TODO 6: Create a variable 'python_version' and set it to 3.11 (float)
python_version= 3.11

# Testing Part 2 - do not modify!
print("\nTesting Part 2...")
try:
    print(f"Student: {student_name}")
    print(f"Grade: {current_grade}")
    print(f"Python version: {python_version}")
    print("Awesome Job! You understand data types!\n")
except NameError as e:
    print("Oops! Something’s missing in Part 2")
    print(f"Error: {e}\n")
    exit()


# ============================================================================
# CONGRATULATIONS!
# ============================================================================
print("=" * 50)
print("CONGRATULATIONS !!! - LEVEL 1 COMPLETE!")
print("=" * 50)
print("\nYou've learned:")
print("How to create and use variables")
print("Different data types (string, int, float)")
print("=" * 50)


