def longest_substring_length(s):
    char_index_map = {}  # Map to store the index of each character in the string
    start = 0  # Start index of the current substring
    max_length = 0  # Maximum length of substring without repeating characters

    for end in range(len(s)):
        # If the current character is already in the substring, update the start index
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        # Update the index of the current character in the map
        char_index_map[s[end]] = end

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, end - start + 1)

    return max_length

# Test the function with the given input
input_str = "pqrsstu"
output = longest_substring_length(input_str)
print(output)
