<h1> Longest Substring </h1>
You are tasked with developing a function that finds the length of the longest substring without repeating characters in a given string s. 
Consider different scenarios involving various characters in the input string.
<br>
<br>
Scenario: String with No Repeating Characters

Input: `abcdef` <br>
Expected Output: `6` <br>
Explanation: In this scenario, the input string contains no repeating characters, so the entire string itself is the longest substring without repeating characters.
<br>
<br>

Scenario: String with Repeating Characters<br>
Input: `abccba` <br>
Expected Output: `3` <br>
Explanation: In this case, the longest substring without repeating characters is "abc" with a length of 3. The characters 'c' and 'b' are repeated, so the substring ends at the first occurrence of the repeated character
<br>
<br>
I
Exercise-1 <br>
Input :
`pqrsstu`

Output :
4
<h1> Simple text Editor </h1>

Create a text editor using commands <br>
<br>
You are developing a text editor that allows users to perform various operations on the text using the "CustomStack" class. The class supports the following operations: <br>
<br>
insert(value): Inserts a string of characters at the current cursor position in the text.
delete(value): Deletes the last value characters from the text starting from the current cursor position.
get(value): Retrieves the character at index value from the text and displays it.
undo(): Reverts the last executed command on the text.
<br>
<br>
Each command is represented by a string in the following format:

1. Command 1: '1 value' - Inserts the string value at the current cursor position in the text. <br>
2. Command 2: '2 value' - Deletes the last value characters from the text starting from the current cursor position.<br>
3. Command 3: '3 value' - Retrieves the character at index value from the text and displays it.<br>
4. Command 4: '4' - Reverts the last executed command on the text.<br>

<br>
Consider a scenario where you have a text editor with a "CustomStack" class that implements the required operations. Assume the initial text is empty.
<br>
Exercise-1 <br>

input:
`1 abc,3 3,2 2,3 1`
<br>
`
Here
1 abc -> command and input text
3 3 -> command and index of the stack`
<br>
Output:
`c
a`
<br>
Exercise-2
Input: ` 1 zxy,3 3,2 2,1 def,3 2`
<br>
Output:
`y
d`
<br>
