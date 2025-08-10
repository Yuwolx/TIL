import sys
sys.stdin = open('input.txt')

# There is a shelf height is B
# N is number of staff
# Each staff's height is indicated Hi
# They are going to make top with themselves 
# If height of top is higher than shelf, they can use items in the shelf
# But more and more high, more risky
# Should be chose the lowest top's hight in top's taller than shelf
# print the smallest gap with B and staff top

# Have to find optimal combination

# How can I solve this problem?
# I need find every combination with staffs
# It is DFS

# When Top height(S) is more than B
# Compare that S with last optimal value
# If now S is lower than last value
# then, now S is new optimal value
# It is branch cutting 

# I need definition function and reculsive functoin to solve thish
# order in solving way
# 1. make comb ordinary
# 2. When S is higher then B, stop
# 3. save that gap
# 3. If gap is smaller than last stored value then store gap in optimal value

def optimal_comb(N,B,staffs):


T = int(input())

for tc in range(1,T+1):
    # N is number of staff
    # B is height of book shelf
    N, B = map(int, input().split())
    
    # create staff's height list
    staffs = list(map(int, input().split()))