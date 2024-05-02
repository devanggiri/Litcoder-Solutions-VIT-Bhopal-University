
# Sliding Subarray Beauty:
You are given an array of integers arr and an integer k. Your task is to find the given n th position of the smallest integer in each contiguous subarray of size k and print these smallest integers.
<br>
<br>
A subarray is a contiguous non-empty sequence of elements within the original array.
For each subarray of size k, you need to find the given n th position of the smallest integer within that subarray.
<br>
<br>
The given n th position of the smallest integer in a subarray is the integer that appears at the given n th position when the subarray is sorted in ascending order.
<br>
<br>
Your task is to return an integer array containing n - k + 1 elements, denoting the beauty of the subarrays in order from the first index in the array.

Exercise-1

Input: 
`1 2 3 4 5 6 7 8 9 10
`
<br>
`3
`
<br>
`2`
<br>
Note: 
Line 1: input array
Line 2: sub array length
Line 3: position of the smallest value

Output:
`2 3 4 5 6 7 8 9
`
# Check string prefix
You are given a list of passwords, where each password consists of lowercase letters from 'a' to 'z' inclusive. The set of passwords is said to be a 'GOOD PASSWORD' if no password is a prefix of another password in the set, except for identical passwords (which are considered prefixes of each other). 
<br>
<br>
In this case, print 'GOOD PASSWORD'. Otherwise, print 'BAD PASSWORD' on the first line, followed by the first pair of passwords where one password is a prefix of the other.
Consider the following list of words: `['apple', 'banana', 'application', 'bananas']`.
<br>
<br>
In this case, the word 'banana' is a prefix of 'bananas'.
<br>
So we would print: `'BAD PASSWORD'`
<br>
<br>
Now let's take another example with a different set of words: ['cat', 'dog', 'elephant']. In this scenario, none of the strings are prefixes of each other.
<br>
<br>
Therefore, we can conclude that: GOOD PASSWORD
<br><br>
Exercise-1

Input:
`abc zxy pqr`

Output:
`GOOD PASSWORD`
