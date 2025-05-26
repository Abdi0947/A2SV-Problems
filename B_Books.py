n,t=map(int,input().split())
a=list(map(int,input().split()))
start = 0
total_time = 0
max_books_read = 0
    
for end in range(n):
        total_time += a[end]
        while total_time > t:
            total_time -= a[start]
            start += 1
        max_books_read = max(max_books_read, end - start + 1)
    
print(max_books_read)
     