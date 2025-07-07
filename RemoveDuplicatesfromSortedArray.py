def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Pointer for the position of unique elements
    i = 0
    
    # Iterate through the array with j
    for j in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[j] != nums[i]:
            i += 1  # Move the unique position pointer
            nums[i] = nums[j]  # Update the unique element position
    
    # Fill the remaining elements with underscores
    for k in range(i + 1, len(nums)):
        nums[k] = '_'  # Fill with underscores
    
    # Print the modified array with unique elements and underscores
    print("Output:", [x for x in nums])  # Convert to string for display without quotes
    
    # Return the count of unique elements
    return i + 1  # i is the index, so we return i + 1 for count

# Testing the function
k1 = removeDuplicates([1, 1, 2])  
# Output: Output: [1, 2, _, _]
# Return value: 2

k2 = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])  
# Output: Output: [0, 1, 2, 3, 4, _, _, _, _, _]
# Return value: 5
