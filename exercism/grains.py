def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)


def total():
    total = 0  # Initialize to 0
    for i in range(1, 65):  # Use range(1, 65) to account for squares 1 through 64
        total += square(i)  # Accumulate grains using square(i)
    return total
