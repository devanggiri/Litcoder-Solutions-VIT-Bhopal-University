import sys

def min_set_size(num, k):
    # If k is 0, a set with only one number '0' will satisfy the condition
    if k == 0:
        return 1 if num == 0 else -1

    # Iterate through possible set sizes starting from 1
    for size in range(1, 11):  # The maximum size can be at most 10 to cover all single-digit numbers
        total = size * k
        if total <= num and (num - total) % 10 == 0:
            return size

    return -1

inputVal1 = input()
inputVal2 = input()
outputVal = min_set_size(inputVal1, inputVal2)
print (outputVal)
                                                                                                                            
