import sys
def check_passwords(passwords):
    passwords.sort()
    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return f'BAD PASSWORD\n{passwords[i]} {passwords[i + 1]}'
    return 'GOOD PASSWORD'

# Example usage:
input_passwords = input().split()
result = check_passwords(input_passwords)
print(result)
            
