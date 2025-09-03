n = int(input())

words = []
for i in range(n):
    x = input()
    words.append(x)


vocas = [[] for _ in range(n)]
alphabet = []
dup = []
for x in range(n):
    for y in words[x]:
        vocas[x].append(y)
        alphabet.append(y)

alphabet = set(alphabet)
lage = len(alphabet)
numbers = [i for i in range(10-lage,10)]

# print(f'words: {words}')
# print(f'vocas: {vocas}')
# print(f'alphabet: {alphabet}')
# print(f'lage: {lage}')
# print(f'numbers:{numbers}')

assign = {}
for x in alphabet:
    assign[x] = 0

# print(f'assign: {assign}')

for x in range(n):
    for y in range(len(vocas[x])):
        assign[vocas[x][y]] += 10**(len(vocas[x]) -1 -y)

nums = list(assign.values())
nums.sort()
# print(f'nums: {nums}')

result = 0
for j in range(lage):
    result += nums[j] * numbers[j]

print(result)
        