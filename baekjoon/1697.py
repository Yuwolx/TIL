n, k = map(int,input().split())
print(f'n,k: {n,k}')

def one_point(n):
    return n + 1

def minus_point(n):
    return n - 1

def double(n):
    return 2*n

# case1 k < n
if k < n:
    c1 = k-n

#case2 need +
c2 = n - k


t = 0
# case3 need x
n3 = n
t3 = t
while n3 < k:
    n3 = double(n3)
    t3 += 1
    if n3 == k:
        print(t3)
        break

#case4 need - * x
n4 = n
t4 = t

#case5 need + * x
n5 = int(n/2)
t5 = t-5