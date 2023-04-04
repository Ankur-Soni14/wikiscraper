# Left triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(j + 65), end="")
    print()

# Left triangle pattern
n = 5
for j in range(n):
    for i in range(j+1):
        print(chr(i + 65), end="")
    print()


# right triangle pattern
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(i + 1):
        print(chr(65 + k), end="")
    print()

# right triangle pattern
size = 5
for j in range(size):
    for i in range(1, size - j):
        print(" ", end="")
    for k in range(j + 1):
        print(chr(65 + k), end="")
    print()
