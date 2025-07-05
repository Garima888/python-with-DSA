def max_integer(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1 * max2
arr = [-1, -4, 4, 7, 8]
result = max_integer(arr)
print("Maximum product of two integers in the array is:" , result)  # output : 56