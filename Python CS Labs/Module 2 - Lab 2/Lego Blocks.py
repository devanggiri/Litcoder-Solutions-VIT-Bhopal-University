import sys
def legoWall(n, m):
    MOD = 1000000007

    # Convert input values to integers
    n, m = int(n), int(m)

    # Create a 3D array to store the number of ways to build the wall
    dp = [[[0] * 4 for _ in range(m)] for _ in range(n + 1)]

    # Initialize base cases
    for i in range(m):
        dp[1][i][0] = 1

    # Populate the array using dynamic programming
    for i in range(2, n + 1):
        for j in range(m):
            for k in range(4):
                dp[i][j][0] += dp[i - 1][j][k]  # Add ways to extend the previous row
                dp[i][j][0] %= MOD

            # If the brick fits horizontally, add ways to place it
            if j > 0:
                for k in range(1, 4):
                    dp[i][j][k] += dp[i][j - 1][0]
                    dp[i][j][k] %= MOD

    # Sum the number of ways to build the wall for each brick type
    result = sum(dp[n][m - 1]) % MOD
    return result

inputVal1 = input()
inputVal2 = input() 
outputVal = legoWall(inputVal1, inputVal2)
print (outputVal)
                                                                                                                            
