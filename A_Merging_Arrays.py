n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

a, b = 0, 0
ans = []

while a < n and b < m:
    if arr1[a] <= arr2[b]:
        ans.append(arr1[a])
        a += 1
    else:
        ans.append(arr2[b])
        b += 1
while a < n:
    ans.append(arr1[a])
    a += 1
while b < m:
    ans.append(arr2[b])
    b += 1
print(*ans)
