n,m = map(int,input().split())
print(f'n,m: {n,m}')

numbers = list(map(int, input().split()))
numbers.sort()
print(f'numbers: {numbers}')

lists = []
each = []

# def make_list(numbers,m):
for i in numbers:
    each.append(i)
    if len(each) == m:
        lists.append(each)
        each = []

