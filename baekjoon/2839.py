N = int(input())

o = 0
os = 0
while os <= N:
    o +=1
    os = o * 5

o -= 1
print(o)
nn = N- o*5
sam = 0
ns = 0
while ns <= nn:
    sam += 1
    ns = sam * 3

sam -= 1
print(sam)
if o*5 + sam*3 == N:
    print(o+sam)
else:
    print(-1) 

