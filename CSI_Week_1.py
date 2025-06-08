n = 7

print("Lower Triangular Pattern:")
for i in range(1, n + 1):
    print("*" * i)

print("\nUpper Triangular Pattern:")
for i in range(n, 0, -1):
    print("*" * i)

print("\nPyramid Pattern:")
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

