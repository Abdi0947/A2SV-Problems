t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = [0, 0, 0]
    for x in a:
        counts[x % 3] += 1  
    target = n // 3
    moves = 0
    for _ in range(2):  
        for i in range(3):
            if counts[i] > target:
                excess = counts[i] - target
                counts[i] -= excess
                counts[(i + 1) % 3] += excess
                moves += excess  
    
    print(moves)
