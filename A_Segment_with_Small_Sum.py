n, s = map(int, input().split())  
a = list(map(int, input().split()))  
start = 0  
current_sum = 0  
max_length = 0  
for end in range(n):
    current_sum += a[end]  
    while current_sum > s:
        current_sum -= a[start] 
        start += 1
    max_length = max(max_length, end - start + 1)

print(max_length)  
