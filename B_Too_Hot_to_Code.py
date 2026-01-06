t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    max_len = 1
    start = 0
    for end in range(1, n):
        if a[end] - a[end - 1] <= k:
            continue
        else:
            max_len = max(max_len, end - start)
            start = end
    max_len = max(max_len, n - start) 
    print(n - max_len)
