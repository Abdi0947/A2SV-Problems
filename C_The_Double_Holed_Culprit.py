n=int(input())
p=list(map(int,input().split()))
result=[]
for start in range(n):
    visited=set()
    current=start
    while current not in visited:
       visited.add(current)
       current=p[current]-1
    result.append(current+1)
print(' '.join(map(str, result)))