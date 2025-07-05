def is_palindrome(x):
    # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10  # Add last digit to reversed_num
        x //= 10  # Remove last digit from x
    
    # Check if the original number is equal to the reversed number
    return x == reversed_num or x == reversed_num // 10

# Testing the function
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome(10))   # Output: False
