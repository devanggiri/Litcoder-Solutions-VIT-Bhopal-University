import sys
def doSomething(nums):
    # Create a hashmap to store the running sum and its corresponding index
    sum_indices = {0: -1}
    
    max_length = 0
    current_sum = 0
    
    for i in range(len(nums)):
        # Update the running sum
        current_sum += 1 if nums[i] == 1 else -1
        
        # If the sum is encountered again, calculate the length of the subarray
        if current_sum in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum])
        else:
            # Store the running sum and its index
            sum_indices[current_sum] = i
    
    return max_length
    
inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)
                        
