# Write a python program to implement the hill climbing algorithm
def hill_climbing(a):
    i = 0
    print("Starting:", a[i])

    while i < len(a) - 1:
        if a[i + 1] > a[i]:
            print(a[i], "->", a[i + 1])
            i += 1
        else:
            print("Stopped at:", a[i])
            break

    return a[i]


a = [1, 2, 3, 4, 6, 4, 3, 9]

result = hill_climbing(a)
print("Final result:", result)