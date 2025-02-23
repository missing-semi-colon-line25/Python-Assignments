def zero_sum(list1):
    sequences = []
    for i in range(len(list1) - 2):
        if list1[i] + list1[i + 1] + list1[i + 2] == 0:
            sequences.append((list1[i], list1[i + 1], list1[i + 2]))
    return sequences

# Example usage
list1 = [1, -1, 0, 2, -2, -2, 4, -4, 1, 0, -1]
result = zero_sum(list1)
print("Sequences where the sum of three consecutive numbers is 0:")
for i in range(len(result)):
    print(f"{i+1}. {result[i]}")
