def removeElement(nums, val):
    if not nums:
            return 0

    pos = 0      
    for i in range(len(nums)):
            if nums[i] != val :
                nums[pos] = nums[i]
                pos += 1
    return pos   
nums = [3, 2, 2, 3]
val = 3  
result = removeElement(nums, val)
print("Output:", nums[:result]) 
print("Return value:", result)  
                
                
