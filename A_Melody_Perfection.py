t = int(input())
for _ in range(t):
    input() 
    notes = list(map(int, input().split()))
    print("YES" if all(abs(notes[i] - notes[i-1]) in (5, 7) for i in range(1, len(notes))) else "NO")
