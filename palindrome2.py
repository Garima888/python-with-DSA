def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert integer to string and check if it is equal to its reverse
    return str(x) == str(x)[::-1]

# Testing the function
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome(10))   # Output: False
