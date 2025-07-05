def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersected = set1.intersection(set2)
    return list(intersected)
arr1 = [1,2,2,3,4]
arr2 = [2,3,5]
result = intersection(arr1,arr2)
print("Intersection of two arrays: ",result)  # output : [2, 3]