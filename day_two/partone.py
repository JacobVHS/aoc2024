def differ_by_one_to_three(num1, num2):
    difference = abs(num1 - num2)
    return 1 <= difference <= 3

# Read input
with open('input') as f:
    lines = f.read().splitlines()

safe_reports = 0

for line in lines:
    numbers = list(map(int, line.split()))
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
            break

    if is_increasing or is_decreasing:
        safe_reports += 1

print(safe_reports)
