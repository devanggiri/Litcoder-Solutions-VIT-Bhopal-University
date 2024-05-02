def query_kth_smallest_trimmed_number(nums, queries):
    answer = []

    for query in queries:
        position, trim_length = query

        # Trim each number to its rightmost trim_length digits
        trimmed_nums = [num[-trim_length:] for num in nums]

        # Determine the index of the kth smallest trimmed number
        sorted_indices = sorted(range(len(trimmed_nums)), key=lambda k: (trimmed_nums[k], k))
        
        # Handle the case where position is out of range
        if position < len(sorted_indices):
            kth_smallest_index = sorted_indices[position]
        else:
            kth_smallest_index = -1  # indicating out of range

        # Reset each number to its original length
        trimmed_nums = [num.zfill(len(num)) for num in trimmed_nums]

        # Store the answer
        answer.append(kth_smallest_index)

    return answer

# Input for numbers
nums_input = input("Enter numbers separated by space: ").split()

# Input for queries
queries_input = []
queries_count = int(input("Enter the number of queries: "))
for _ in range(queries_count):
    query = tuple(map(int, input("Enter query (position, trim length): ").split()))
    queries_input.append(query)

# Call the function with user input
output_result = query_kth_smallest_trimmed_number(nums_input, queries_input)

# Display the output
print(*output_result)
