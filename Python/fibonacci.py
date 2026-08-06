def generate_fibonacci(terms):
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < terms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example Usage
num_terms = 10
print(f"Fibonacci sequence ({num_terms} terms): {generate_fibonacci(num_terms)}")
