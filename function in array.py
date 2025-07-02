# Problem 1: Array Basics
arr = [10, 20, 30, 40, 50]

# Print the second element
print("Second element:", arr[1])

# Add a new integer to the end
arr.append(60)
print("Array after adding 60:", arr)

# Remove the first element
arr.remove(arr[0])
print("Array after removing first element:", arr)

# Problem 2: Array Operations
def find_max(arr):
    return max(arr)

def reverse_array(arr):
    return arr[::-1]

def is_sorted(arr):
    return arr == sorted(arr)

# Testing the functions
print("Maximum element:", find_max(arr))
print("Reversed array:", reverse_array(arr))
print("Is array sorted?", is_sorted(arr))
