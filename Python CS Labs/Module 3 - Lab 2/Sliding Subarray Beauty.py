import sys

def sliding_subarray_beauty(arr, k, n):
    result = []

    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        sorted_subarray = sorted(subarray)
        result.append(sorted_subarray[n - 1])

    return result

# Example usage:
input_array = list(input())
subarray_length = int(input())
position_of_smallest = int(input())

output_array = sliding_subarray_beauty(input_array, subarray_length, position_of_smallest)
print(output_array)

                   
