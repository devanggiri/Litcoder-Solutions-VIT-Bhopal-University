def maximize_subsequences(text, pattern):
    # Count occurrences of pattern[0] and pattern[1] in the original text
    count_pattern_0 = text.count(pattern[0])
    count_pattern_1 = text.count(pattern[1])

    # Calculate the maximum occurrences if pattern[0] is inserted
    max_occurrences_with_pattern_0 = (count_pattern_0 + 1) * count_pattern_1

    # Calculate the maximum occurrences if pattern[1] is inserted
    max_occurrences_with_pattern_1 = (count_pattern_1 + 1) * count_pattern_0

    # Return the maximum of the two possibilities
    return max(max_occurrences_with_pattern_0, max_occurrences_with_pattern_1)

# Test the function with the given inputs
input_text_1 = "ababc"
input_pattern_1 = "ab"
output_1 = maximize_subsequences(input_text_1, input_pattern_1)
print(output_1)

input_text_2 = "ababab"
input_pattern_2 = "ab"
output_2 = maximize_subsequences(input_text_2, input_pattern_2)
print(output_2)
