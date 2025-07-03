#Array Manipulation
def second_largest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[-2] if len(unique_elements) >= 2 else None

def remove_duplicates(arr):
    return list(set(arr))

# Testing the functions
arr = [10, 20, 20, 30, 40]
print("Second largest element:", second_largest(arr))
print("Array after removing duplicates:", remove_duplicates(arr))

