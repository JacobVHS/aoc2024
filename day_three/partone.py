import re

with open('input') as f:
    text = f.read().splitlines()
pattern = r"mul\((\d+),(\d+)\)"

total = []

for line in text:
    matches = re.findall(pattern, line)
    total.extend(matches)

sum = 0

for pair in total:
    print("Processing:",pair)
    multiply = int(pair[0]) * int(pair[1])
    sum = sum + multiply

print("Sum is ", sum)