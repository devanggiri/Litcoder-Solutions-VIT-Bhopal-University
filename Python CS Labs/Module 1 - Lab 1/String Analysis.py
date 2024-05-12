import sys
def doSomething(inval):
    
    upper_case = 0
    lower_case = 0 
    digit = 0
    other = 0
    
    for char in inval:
        if char.isupper():
            upper_case +=1
        elif char.islower():
            lower_case +=1
        elif char.isdigit():
            digit +=1
        else:
            other +=1
    
    total_length = len(inval)
    
    u_100 = (upper_case/total_length) * 100
    l_100 = (lower_case/total_length) * 100
    d_100 = (digit/total_length) * 100
    o_100 = (other/total_length) * 100
    
    outval = (
        f"Uppercase letters: {u_100:.3f}%\n"
        f"Lowercase letters: {l_100:.3f}%\n"
        f"Digits: {d_100:.3f}%\n"
        f"Other characters: {o_100:.3f}%"
    )

    return outval
inputVal = input()    
outputVal = doSomething(inputVal)
print(outputVal)
                                                                                                                            
