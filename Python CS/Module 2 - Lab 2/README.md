<h1>Sum of Numbers With Units Digit K</h1>
<br>
You are given two integers, num and k. You need to find the minimum possible size of a set of positive integers with the following properties:
<br>
<br>
-  Each integer in the set has the unit digit equal to k. <br>
-  The sum of all the integers in the set equals num.
<br>
If such a set exists, return its minimum size. Otherwise, if no set satisfies the conditions, return -1.
<br>
<br>

```Note:```
<br>
<br>
The set can contain multiple instances of the same integer, and if the set is empty, its sum is considered to be 0.<br>
The unit digit of a number refers to its rightmost digit.<br>
<br>
<br>
Consider the input:
<br>
<br>
num = `58` <br>
k = `9`
<br>
<br>
The function should return 2 because there exists a valid set with two positive integers, both having the units digit 9, and their sum is equal to 58.
<br>
<br>
Exercise-1
<br>
<br>
Input :
`56
9
`
<br>
Output :
`4`
<br>

<h1>Lego Blocks</h1>

Build a wall with lego blocks <br>
How many different ways can you build a wall of height 'n' and width 'm' using an infinite number of Lego bricks of four types, each with different dimensions (depth x height x width)? 
<br>
<br>
The types of Lego bricks available are:
<br>
<br>
-  Depth: 1, Height: 1, Width: 1 <br>
-  Depth: 1, Height: 1, Width: 2 <br>
-  Depth: 1, Height: 1, Width: 3 <br>
-  Depth: 1, Height: 1, Width: 4
<br>
<br>

The wall should satisfy the following conditions:
<br>
<br>
-  There should be no holes in the wall.<br>
-  The wall should be a single solid structure without a straight vertical break across all rows of bricks.<br>
-  The bricks must be laid horizontally.<br>
-  Provide the number of ways to build the wall, considering that the result should be output modulo `1000000007`.<br>

<br>
<br>
Example:
<br>
<br>
-  For n = 2 and m = 2, the output should be legoWall(n, m) = 3. <br>
-  For n = 3 and m = 2, the output should be legoWall(n, m) = 7. <br>
-  For n = 2 and m = 3, the output should be legoWall(n, m) = 9. 
<br>
<br>

Input/Output:
<br>
<br>
1.  The input consists of two integers: n and m, representing the desired height and width of the wall, respectively. <br>
2.  The output is a long integer representing the number of ways to build the wall, modulo 1000000007. <br>

<br>

Exercise-1
<br>
Input:
`
2
2
`
<br>
<br>

Here
First row - n value <br>

Second row - m value <br>

<br>
Output:

`3`
