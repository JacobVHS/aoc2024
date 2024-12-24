import time

# Start the timer
start = time.time()

# Read and process input
with open("input", "r") as f:
    line = f.read().strip()

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

# Process the disk to resolve "X"
while "X" in disk:
    # Remove trailing "X"
    while disk and disk[-1] == "X":
        disk.pop()
    if "X" in disk:
        first_dot = disk.index("X")
        disk[first_dot] = disk[-1]
        disk.pop()

# Calculate the total
total = sum(i * ord(c) for i, c in enumerate(disk))

# End the timer
end = time.time()

# Output the results
print(total)
print(f"time: {end - start:.2f}s")
