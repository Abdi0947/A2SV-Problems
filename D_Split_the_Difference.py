n, k = map(int, input().split())
a = list(map(int, input().split()))

cost = a[-1] - a[0]
gaps = []

for i in range(n - 1):
    gaps.append(a[i + 1] - a[i])

gaps.sort(reverse=True)
cost -= sum(gaps[:k - 1])

print(cost)
