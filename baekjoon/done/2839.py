N = int(input())
nn = N
# o = count(5), os = sum(5)
# s = count(3), ss = sum(s)
o = 0
os = 0
s = 0
ss = 0
rn = N
lists = []
while rn > 0:
    if rn % 3 == 0:
        lists.append(rn//3 + o)
    rn -= 5
    o += 1
    if rn == 0:
        lists.append(o)

if len(lists) == 0:
    print(-1)
else:
    print(min(lists))