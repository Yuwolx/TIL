n,k = map(int, input().split())

items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append([w,v])

max_val = [0 for _ in range(k+1)]

for w, v in items:
    #print(f'w,v: {w,v}')
    for i in range(k,w-1, -1):
        max_val[i] = max(max_val[i], v + max_val[i-w])
   #print(max_val)

print(max(max_val))