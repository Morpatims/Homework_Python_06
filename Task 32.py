def find_indices_in_range(my_list, min_val, max_val):
    indices = []
    for i, element in enumerate(my_list):
        if min_val <= element <= max_val:
            indices.append(i)
    return indices

num_elements = int(input("Enter the number of items in the list: "))
indices = []
for i in range(num_elements):
    element = float(input(f"Enter an element #{i + 1}: "))
    indices.append(element)
min_val = float(input("Enter the minimum value: "))
max_val = float(input("Enter the maximum value: "))

print(find_indices_in_range(indices, min_val, max_val))