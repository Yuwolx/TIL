def fibonacci_memoization(n):

    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    # if when you carculate that, use that directly
    return memo[n]

# record fibonacci result to 10
n = 10
memo = [0] * (n+1)
memo[0], memo[1] = 0,1 #reset basic rule