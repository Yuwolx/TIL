n, m = map(int,input().split())

visited = [False] * (n+1)
plans = []
dep = 0

def make_list(dep):
    if dep == m:
        print(*plans)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            plans.append(i)
            make_list(dep+1)
            plans.pop()
            visited[i] = False

make_list(dep)