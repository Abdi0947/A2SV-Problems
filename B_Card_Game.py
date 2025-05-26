n = int(input())
arr = list(map(int, input().split()))
pairs= [(val, key + 1) for key, val in enumerate(arr)]
pairs.sort()
for i in range(n//2):
    print(pairs[i][1], pairs[n - i - 1][1])
