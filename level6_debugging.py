
# Global data
liquids = ["Water", "Mercury", "Ethanol", "Nitrogen", "Oxygen"]
freezing_points = [0, -39, -114, -210, -218]
boiling_points = [100, 357, 78, -196, -183]

# ============================================================================
# BUG 1: Missing colon in function definition
# ============================================================================
def display_welcome():  # BUG HERE - Missing colon
    print("Welcome to the Liquid State Analyzer!")
    print("This program has bugs - can you find them all?")

# ============================================================================
# BUG 2: Wrong indentation
# ============================================================================
def display_all_liquids():
    print("\nAvailable liquids:")
    for i in range(len(liquids)):
        print(f"{i+1}. {liquids[i]}")  # BUG HERE - Wrong indentation

# ============================================================================
# BUG 3: Wrong comparison operator
# ============================================================================
def get_state(temperature, freezing_point, boiling_point):
    if temperature < freezing_point:
        return "Solid"
    elif temperature > boiling_point:  # BUG HERE - Should be < not >
        return "Gas"
    else:
        return "Liquid"

# ============================================================================
# BUG 4: Wrong list index (off by one error)
# ============================================================================
def get_liquid_name(choice):
    # User enters 1-5, but lists start at 0
    return liquids[choice-1]  # BUG HERE - Should be choice - 1

# ============================================================================
# BUG 5: Swapped return values
# ============================================================================
def calculate_distances(temperature, freezing_point, boiling_point):
    distance_from_freezing = temperature - freezing_point
    distance_from_boiling = boiling_point - temperature
    
    # BUG HERE - These are swapped!
    return distance_from_freezing, distance_from_boiling

# ============================================================================
# BUG 6: Variable name typo
# ============================================================================
def display_liquid_info(liquid_index):
    liquid_name = liquids[liquid_index]
    freezing = freezing_points[liquid_index]
    boiling = boiling_points[liquid_index]
    
    print(f"\nLiquid Information:")
    print(f"Name: {liquid_name}")
    print(f"Freezing Point: {freezing}°C")  # BUG HERE - Typo in variable name
    print(f"Boiling Point: {boiling}°C")

# ============================================================================
# BUG 7: Forgot to convert input to int
# ============================================================================
def get_user_choice():
    display_all_liquids()
    choice = int(input("\nSelect a liquid (1-5): "))  # BUG HERE - Should convert to int
    return choice

# ============================================================================
# BUG 8: Missing 'f' in f-string
# ============================================================================
def display_state_analysis(liquid_name, temperature, state):
    print(f"\nANALYSIS COMPLETE!")
    print("=" * 50)
    print("At {temperature}°C, {liquid_name} is: {state}")  # BUG HERE - Missing f before string
    print("=" * 50)

# ============================================================================
# BUG 9: Index out of range
# ============================================================================
def compare_all_liquids(temperature):
    print(f"\nAll liquids at {temperature}°C:")
    for i in range(len(liquids) -1):  # BUG HERE - Goes one past the end of list
        state = get_state(temperature, freezing_points[i], boiling_points[i])
        print(f"  {liquids[i]}: {state}")

# ============================================================================
# BUG 10: Using string as list index
# ============================================================================
def get_temperature_range(liquid_index):
    boiling = boiling_points[liquid_index]
    freezing = freezing_points[liquid_index]
    range_value = boiling - freezing
    
    # Create a string that shows the range
    range_string = (f"{range_value}")
    
    # BUG HERE - Trying to use string as index
    test_value = liquids[range_string]
    
    return range_value

# ============================================================================
# MAIN PROGRAM
# ============================================================================
def run_analyzer():
    display_welcome()
    
    # Get user's choice
    choice = get_user_choice()
    liquid_index = choice - 1
    
    # Get liquid name
    liquid_name = get_liquid_name(choice)
    
    # Display liquid info
    display_liquid_info(liquid_index)
    
    # Get temperature
    temperature = float(input("\nEnter temperature in Celsius: "))
    
    # Analyze the state
    state = get_state(
        temperature,
        freezing_points[liquid_index],
        boiling_points[liquid_index]
    )
    
    # Display results
    display_state_analysis(liquid_name, temperature, state)
    
    # Show distances
    dist_freeze, dist_boil = calculate_distances(
        temperature,
        freezing_points[liquid_index],
        boiling_points[liquid_index]
    )
    
    print(f"\nTemperature Distances:")
    print(f"Distance from freezing: {dist_freeze}°C")
    print(f"Distance from boiling: {dist_boil}°C")
    
    # Get temperature range (this will cause bug 10)
    try:
        temp_range = get_temperature_range(liquid_index)
        print(f"\nTemperature range for {liquid_name}: {temp_range}°C")
    except:
        print("\nBug 10 still needs fixing in get_temperature_range function!")
    
    # Compare all liquids (this will cause bug 9)
    try:
        compare_all_liquids(temperature)
    except:
        print("\nBug 9 still needs fixing in compare_all_liquids function!")
    
    print("\n" + "=" * 50)
    print("Thank you for debugging!")
    print("=" * 50)

# ============================================================================
# START THE PROGRAM
# ============================================================================
if __name__ == "__main__":
    print("DEBUG CHALLENGE: Find and fix all 10 bugs!")
    print("TIP: Fix ONE bug at a time, then run the program again.\n")
    
    try:
        run_analyzer()
        
        print("\n" + "=" * 50)
        print("LEVEL 6 COMPLETE!")
        print("=" * 50)
        print("\nYou've learned:")
        print("How to read error messages")
        print("How to fix syntax errors")
        print("How to fix logic errors")
        print("How to fix index errors")
        print("How to debug systematically")
        print("\nCongratulations! You've completed all debugging challenges!")
        print("You're now ready to build your own Python projects!")
        print("=" * 50)

    except Exception as e:
        print(f"\nERROR FOUND!")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {e}")
        print("\nRead the error message carefully - it tells you what's wrong!")
        print("Fix the bug and run the program again.")