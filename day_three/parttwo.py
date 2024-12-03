import re

with open('input') as f:
    text = f.read()  # Read the whole file content at once (this took me a minute to realise I had to do haha)

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

total = []
include_mul = True

index = 0
while index < len(text):

    if text[index:index+4] == "do()":
        include_mul = True
        index += 4
        continue

    elif text[index:index+7] == "don't()":
        include_mul = False
        index += 7
        continue

    match = re.match(mul_pattern, text[index:])
    if include_mul and match:
        num1, num2 = int(match.group(1)), int(match.group(2))
        total.append((num1, num2))
        index += len(match.group(0))
        continue

    index += 1

sum_result = 0
for pair in total:
    print("Processing:", pair)
    multiply = pair[0] * pair[1]
    sum_result += multiply

print("Sum is", sum_result)

