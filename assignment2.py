def fibonacci(n):
    # Handle special cases for n less than or equal to 0
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Start the sequence with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    for i in range(2, n):
        # Add the sum of the last two numbers to the sequence
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence
