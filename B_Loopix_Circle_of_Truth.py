t = int(input())
for val in range(t):
    s = input().strip()
    k = s.count('N')
    if k == 1:
        print("NO")
    else:
        print("YES")
