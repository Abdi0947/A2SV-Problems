from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)
    score = sum(v // 2 for v in count.values())
    print(score)
