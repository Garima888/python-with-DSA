def rotation_array(arr, d):
    for i in range(len(arr)):
        if i < d:
            print(arr[i + len(arr) - d], end=' ')
        else:
            print(arr[i - d], end=' ')
# Example usage

arr = [10,20,30,40,50]
rotation_array(arr,2)    
