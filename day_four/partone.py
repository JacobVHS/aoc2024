# Read puzzle input
with open('input') as f:
    text = f.read().splitlines()

# length of line and total lines
char_length = len(text[0])
total_lines = len(text)

# initialize sum
sum = 0

for x in range(total_lines):
    # grab the current line
    line = text[x]

    for i in range(char_length):
        # set the letter we are on
        current_letter = line[i]

        if current_letter == 'X': 
            # Check horizontally forward
            if i + 3 < char_length:
                forward_word = (current_letter, line[i+1], line[i+2], line[i+3])
                if ''.join(forward_word) == "XMAS":
                    sum += 1
            
            # Check horizontally backward
            if i - 3 >= 0:
                backward_word = (current_letter, line[i-1], line[i-2], line[i-3])
                if ''.join(backward_word) == "XMAS":
                    sum += 1

            # Check vertically down
            if x + 3 < total_lines:
                down_word = (current_letter, text[x+1][i], text[x+2][i], text[x+3][i])
                if ''.join(down_word) == "XMAS":
                    sum += 1

            # Check vertically up
            if x - 3 >= 0:
                up_word = (current_letter, text[x-1][i], text[x-2][i], text[x-3][i])
                if ''.join(up_word) == "XMAS":
                    sum += 1

            # Check diagonally down-right
            if x + 3 < total_lines and i + 3 < char_length:
                down_right_word = (current_letter, text[x+1][i+1], text[x+2][i+2], text[x+3][i+3])
                if ''.join(down_right_word) == "XMAS":
                    sum += 1

            # Check diagonally up-left
            if x - 3 >= 0 and i - 3 >= 0:
                up_left_word = (current_letter, text[x-1][i-1], text[x-2][i-2], text[x-3][i-3])
                if ''.join(up_left_word) == "XMAS":
                    sum += 1

            # Check diagonally down-left
            if x + 3 < total_lines and i - 3 >= 0:
                down_left_word = (current_letter, text[x+1][i-1], text[x+2][i-2], text[x+3][i-3])
                if ''.join(down_left_word) == "XMAS":
                    sum += 1

            # Check diagonally up-right
            if x - 3 >= 0 and i + 3 < char_length:
                up_right_word = (current_letter, text[x-1][i+1], text[x-2][i+2], text[x-3][i+3])
                if ''.join(up_right_word) == "XMAS":
                    sum += 1

# Print the total count of "XMAS"
print(sum)
