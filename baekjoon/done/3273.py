n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
result = 0

'''
whether = [0 for _ in range(2000000)]
for x in numbers:
    if x == target: continue
    if whether[x] == 1:
        result += 1
    else:
        whether[target-x] = 1
'''
'''
seen = set()
for x in numbers:
    if x in seen:
        result += 1
    else:
        seen.add(target)
'''

print(result)
