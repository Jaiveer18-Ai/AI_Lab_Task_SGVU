
def minimax(scores, depth, node_index, is_max):
    if depth == 0:
        return scores[node_index]

    left = minimax(scores, depth - 1, node_index * 2, not is_max)
    right = minimax(scores, depth - 1, node_index * 2 + 1, not is_max)

    if is_max:
        return max(left, right)
    return min(left, right)


print("=" * 35)
print("       MINIMAX ALGORITHM")
print("=" * 35)

depth = int(input("Enter tree depth: "))
count = 2 ** depth

scores = list(map(int, input(f"Enter {count} elements: ").split()))

result = minimax(scores, depth, 0, True)

print("-" * 35)
print("Optimal value:", result)
print("=" * 35)
