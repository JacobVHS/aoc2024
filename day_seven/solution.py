with open("input", "rt") as file:
    lines = [line.strip() for line in file]

def generate_ops_sequences(length, operators):
    """Generate all operator sequences of a given length."""
    if length == 1:
        return operators
    sequences = []
    for seq in generate_ops_sequences(length - 1, operators):
        for op in operators:
            sequences.append(seq + op)
    return sequences

def calculate_expression(numbers, operators):
    """Evaluate the expression represented by numbers and operators."""
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i + 1]
        elif operator == "*":
            result *= numbers[i + 1]
        else:  # Concatenate numbers
            result = int(str(result) + str(numbers[i + 1]))
    return result

def solve_line(line, operators):
    """Solve a single line for the required result."""
    target, expression = line.split(": ")
    target = int(target)
    numbers = tuple(map(int, expression.split()))
    for ops_sequence in generate_ops_sequences(len(numbers) - 1, operators):
        if calculate_expression(numbers, ops_sequence) == target:
            return target
    return 0

print(sum(solve_line(line, "+*") for line in lines))
print(sum(solve_line(line, "+*&") for line in lines))
