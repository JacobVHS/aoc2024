def differ_by_one_to_three(num1, num2):
    difference = abs(num1 - num2)
    return 1 <= difference <= 3

def is_safe_sequence(numbers):
    is_increasing = True
    is_decreasing = True
    
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        
        # Check increasing condition
        if diff < 0 or not differ_by_one_to_three(numbers[i], numbers[i + 1]):
            is_increasing = False
        
        # Check decreasing condition
        if diff > 0 or not differ_by_one_to_three(numbers[i], numbers[i + 1]):
            is_decreasing = False
        
        # If neither condition is satisfied, break early
        if not is_increasing and not is_decreasing:
            return False

    return is_increasing or is_decreasing

# Check if removing one number makes it a safe sequence
def can_be_safe_by_removal(numbers):
    for i in range(len(numbers)):
        # Create a new list with the ith number removed
        modified_numbers = numbers[:i] + numbers[i+1:]
        if is_safe_sequence(modified_numbers):
            return True
    return False

# Read input
with open('input') as f:
    lines = f.read().splitlines()

safe_reports = 0

for line in lines:
    numbers = list(map(int, line.split()))
    
    # Check if the sequence itself is safe or can be made safe by removing one number
    if is_safe_sequence(numbers) or can_be_safe_by_removal(numbers):
        safe_reports += 1

print(safe_reports)
