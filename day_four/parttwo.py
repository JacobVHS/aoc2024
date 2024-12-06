# Read puzzle input
with open('input') as f:
    text = f.read().splitlines()

# Length of line and total lines
char_length = len(text[0])
total_lines = len(text)

# Initialize sum
sum = 0

for x in range(total_lines):
    for i in range(char_length):
        # Check for the center 'A' in the X-MAS pattern
        if text[x][i] == 'A':
            # Ensure all diagonals are within bounds
            if (
                x - 1 >= 0 and i - 1 >= 0 and  # Up-left
                x + 1 < total_lines and i + 1 < char_length and  # Down-right
                x - 1 >= 0 and i + 1 < char_length and  # Up-right
                x + 1 < total_lines and i - 1 >= 0  # Down-left
            ):
                # Get diagonal letters
                up_left = text[x-1][i-1]
                down_left = text[x+1][i-1]
                up_right = text[x-1][i+1]
                down_right = text[x+1][i+1]

                # Check both diagonals for "MAS" pattern
                diagonal_1 = {up_left, down_right}
                diagonal_2 = {down_left, up_right}

                # Both diagonals must independently form {M, S}
                if diagonal_1 == {'M', 'S'} and diagonal_2 == {'M', 'S'}:
                    sum += 1

# Print the total count of X-MAS patterns
print(sum)