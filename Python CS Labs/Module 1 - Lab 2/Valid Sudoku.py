import sys
def doSomething(board):
    # Check Rows
    for row in board:
        if not is_valid_group(row):
            return False
    
    # Check Columns
    for col in zip(*board):
        if not is_valid_group(col):
            return False
    
    # Check Sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_group(sub_box):
                return False
    
    return True

def is_valid_group(group):
    # Helper function to check if a group (row, column, or sub-box) is valid
    seen = set()
    for num in group:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)
                                                                                                                            
