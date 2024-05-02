<h1>Valid Sudoku</h1>
Sudoku board validation algorithm 
<br>
<br>
You have been tasked with developing an algorithm to validate a 9 x 9 Sudoku board. Your algorithm needs to verify the validity of the filled cells on the board, adhering to the following conditions:
<br>
<br>
-  Every row should contain the numbers 1-9 exactly once, without repetition.<br>
-  Every column should contain the numbers 1-9 exactly once, without repetition.<br>
-  Each of the nine 3 x 3 sub-boxes within the grid should contain the numbers 1-9 exactly once, without repetition.<br>
<br>
Can you outline an algorithm or a step-by-step approach to determine if the given Sudoku board configuration is valid based on these conditions?
<br>
<br>

Exercise-1
<br>
<br>
Input :

`
9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
`
<br>
Output :
`
YES
`
<br>
<br>
Exercise-2
<br>
Input:
`
9
5 3 . . 7 . . . .
5 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
`
<br>
Output:
NO



<h1>Queue using Two Stacks</h1>
<br>
Write a program to implement a custom queue using two stacks. The queue should support the following three types of queries:
<br>
<br>
<strong>Enqueue:</strong> This query type is denoted by "1 x", where x is an element to be enqueued. It means that you need to insert element x at the end of the queue.
<br>
<strong>Dequeue:</strong> This query type is denoted by "2". It indicates that you should remove the element at the front of the queue.
<br>
<strong>Print Front:</strong> This query type is denoted by "3". It instructs you to print the element at the front of the queue without removing it.
<br>
<br>
Exercise-1
<br>

input:
`
1 42,2,1 14,3
`
<br>
output:
`
14
`
<br>
<br>
Exercise-2
<br>
input:
`
1 23,2,1 14,3,2,1 78,3
`
<br>
Output:
`
14
78
`
