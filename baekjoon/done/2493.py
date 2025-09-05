
'''
There is N tower have different height
Each tower shot raiser to left side
Just one top taller than originated top recieve raiser
Write recieve top's index at shoot top's location
'''
'''
1. pop for visit
2. investigate there is tower can recieve raiser
3. if there is no tower or only smaller tower, return 0

'''


N = int(input())
towers = list(map(int,input().split()))
stack = []
result = []

for x in range(N):
    invest = towers[x]
    while stack and stack[-1][0] < invest:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1])

    stack.append([invest,x+1])



print(*result)