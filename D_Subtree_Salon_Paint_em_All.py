n = int(input())
parents = list(map(int, input().split()))
colors = list(map(int, input().split()))

steps = 1
for i in range(1, n):
    parent = parents[i-1] - 1
    if colors[i] != colors[parent]:
        steps += 1
print(steps)
