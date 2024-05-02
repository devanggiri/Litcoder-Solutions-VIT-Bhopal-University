
<h1>Maximize Subsequences in String</h1>
You are given two strings, **text** and **pattern**, both consisting of only lowercase English letters.
<br>

The objective is to modify the text by adding either `pattern[0]` or `pattern[1]` exactly once at any position. 
After the modification, you need to determine the maximum number of times the pattern can occur as a subsequence in the modified text.
A subsequence is a sequence of characters obtained by deleting some or no characters from the original sequence without changing the order of the remaining characters.
<br>

Example with Explanation<br>
Input text is `“abdcdbc”.` Input Pattern is `“ac”`. <br>
When inserting `'a'` as Pattern [0] between text [1] and text [2], the resulting string is "abadcdbc."
<br>
<br>
After deleting `“bd”` in the newly created text, we will get “aacc”. In this modified string, the subsequence "ac" appears four times. <br>

Some other combinations are,
1.  aabdcdbc -> aacc -> Four times<br>
2.  abdacdbc -> aacc-> Four times<br>
3.  abdcadbc -> acac -> Three times<br>
4.  abdccdbc -> accc -> Three times<br>
5.  abdcdbcc -> accc -> Three times<br>

<br>
<br>

Input and Output format:
<br>
Exercise-1
<br>
Input: 

`
ababc` <br>
`
ab
`
<h1>Cookies</h1>

Candies
You have a collection of candies, and each candy has a certain sweetness value. Your goal is to combine the candies to create new candies until you reach a specific target sweetness level. Find how many steps need to reach candies sweetness target.
<br>
To achieve this, you can select any two candies with the least sweetness and combine them into a new candy with sweetness calculated as follows:
<br>
<br>
sweetness = (least sweet candy + 2 * second least sweet candy)
<br><br>
For example, consider the following scenario:
<br>
You are given a target sweetness level of 12, and you have the following candies: [2, 8, 3, 7, 4, 6]. To reach the target sweetness of 12.
<br><br>
you can perform the following steps:
<br>
Ascending order = 2,3,4,6,7,8
<br>
<br>
Combine the two least sweet candies: 2 + 2*3 = 8. Updated candies: [ 8, 4, 6, 7, 8]. <br>
Combine the two least sweet candies: 4 + 2*6 = 16. Updated candies: [8, 16, 7, 8]. <br>
Combine the two least sweet candies: 7 + 2*8 = 23. Updated candies: [8,16,23]. <br>
Combine the two least sweet candies: 8 + 2*16 = 17. Updated candies: [40,23]. <br>
<br>
<br>
The sweetness of the first candy in the updated candies array is now 40, which exceeds the target sweetness of 12.
<br>
Exercise-1
<br>
<br>
Input:
<br>
`
7
`
<br>
`
1 2 3 4 5
`
<br>
Note:
<br>
<br>
Line 1 : Target of the sweetness
Line 2 Each candies sweetness
<br>
output:<br>
`
3
`
<br>
<br>
Exercise-2
<br>
Input:
<br>
`
11
`
`
2 5 3 7 6 1
`
<br>
output:
<br>
`
4
`
<br>
Output:
<br>

`
5
`
