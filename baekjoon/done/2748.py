

# n = int(input())
# fibo = [0] * (n+1)
# fibo[0] = 0
# fibo[1] = 1
# for i in range(n+1):
#     if i == 0 or i == 1:
#         continue
#     fibo[i] = fibo[i-1] + fibo[i-2]

# print(fibo[n])

n = int(input())
a, b = 0, 1
for _ in range(n//2):
    a = a + b
    b = a + b

if n % 2 == 0:
    print(a)
else:
    print(b)