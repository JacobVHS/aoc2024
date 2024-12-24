import time

# Read and process input
with open("input", "r") as f:
    line = f.read().strip()

start = time.time()

disk = []
empty = False
char_index = 0

# Generate the initial disk content
for char in line:
    count = int(char)
    if empty:
        disk.extend("X" * count)
    else:
        disk.extend(chr(char_index) * count)
        char_index += 1
    empty = not empty

# Remove trailing "X"
while disk and disk[-1] == "X":
    disk.pop()

# Get list of files without spaces
files = []
last_char = disk[0]
file_length = 0

for i, char in enumerate(disk):
    if char != last_char:
        if last_char != "X":
            files.append((last_char * file_length, i - file_length))
        file_length = 1
    else:
        file_length += 1
    last_char = char

len_disk = len(disk)
if last_char != "X":
    files.append((last_char * file_length, len(disk) - file_length))

# Move files into spaces
while files:
    length_last = len(files[-1][0])  # Get length of the last file
    try:
        # Find the first space with enough capacity
        first_space = "".join(disk).index("X" * length_last, 0, files[-1][1])
    except ValueError:
        files.pop()
        continue

    # Move the last file into the space
    disk = (
        disk[:first_space]
        + list(files[-1][0])
        + disk[first_space + length_last : files[-1][1]]
        + ["X"] * length_last
        + disk[files[-1][1] + length_last :]
    )

    # Remove the last file from the list
    files.pop()

# Calculate the total
total = sum(i * ord(c) for i, c in enumerate(disk) if c != "X")

end = time.time()

# Output the results
print(total)
print(f"time: {end - start:.2f}s")
