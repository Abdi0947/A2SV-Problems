t = int(input())
for _ in range(t):
    n = int(input())
    m = (n - 1) // 2
    
    total_moves = 0
    for k in range(1, m + 1):
        total_moves += 8 * k * k
    
    print(total_moves)
