def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        current_value = roman_numerals[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
            
        prev_value = current_value
        
    return total
print(roman_to_int("III"))      # Output: 3
print(roman_to_int("IV"))       # Output: 4     
print(roman_to_int("IX"))       # Output: 9
print(roman_to_int("LVIII"))    # Output: 58    
