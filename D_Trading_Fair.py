import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
result = []

for x in b:
    count = bisect.bisect_right(a, x)
    result.append(count)

print(*result)
