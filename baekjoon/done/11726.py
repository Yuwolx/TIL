# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5

n = int(input())

a ,b = 0, 1
for _ in range(n+1):
    a ,b = a+b, a

print(a % 10007)
