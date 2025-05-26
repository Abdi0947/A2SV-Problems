t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split())) 
    fav_value = a[f - 1] 
    sorted_a = sorted(a, reverse=True)
    count_greater = sum(1 for num in sorted_a if num > fav_value)
    count_equal = sum(1 for num in sorted_a if num == fav_value)
    low = count_greater + 1
    high = count_greater + count_equal
    if high <= k:
        print("YES")  
    elif low > k:
        print("NO")  
    else:
        print("MAYBE")  