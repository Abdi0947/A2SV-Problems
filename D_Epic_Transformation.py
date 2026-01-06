from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = Counter(a)
    maxi = max(freq.values())

    if maxi <= n // 2:
        mini = n % 2  
    else:
        mini = 2 * maxi - n
    
    print(mini)  
