n = int(input())
c = list(map(int, input().split()))
g = [] 
cnt = 1
for i in range(1, n):
    if c[i] == c[i-1]:
        cnt += 1
    else:
        g.append(cnt)
        cnt = 1
g.append(cnt) 
ans = 0
for i in range(len(g)-1):
    ans = max(ans, 2 * min(g[i], g[i+1]))
print(ans)
