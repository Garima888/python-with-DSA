def sum_two(arr, target):
    if len(arr) < 2:
        return None
    else :
     for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
              return list[i,j]
     return None      
arr = [1, 2, 3, 4, 5] 
target = 9
result = sum_two(arr, target)           
print("Indices of the two integers that sum to target:", result)  # Output: [3, 4]
