t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    unsorted_possible = False
    
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            unsorted_possible = True
            break
    
    if unsorted_possible:
        print("YES")
    else:
        print("NO")
