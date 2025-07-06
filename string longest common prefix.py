def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the initial prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for s in strs[1:]:
        while not s.startswith(prefix):
            # Shorten the prefix until it matches
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))      # Output: ""
print(longest_common_prefix([""]))                             # Output: ""     
print(longest_common_prefix(["good", "goodness", "goodservice", "goodwill"]))    # Output: "good"