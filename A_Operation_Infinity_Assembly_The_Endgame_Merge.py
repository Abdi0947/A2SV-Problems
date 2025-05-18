def solve():
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())

    c = []
    a_count = 0
    b_count = 0
    a_ptr = 0
    b_ptr = 0

    while a_ptr < n and b_ptr < m:
        if a[a_ptr] < b[b_ptr]:
            if a_count < k:
                c.append(a[a_ptr])
                a_ptr += 1
                a_count += 1
                b_count = 0
            else:
                c.append(b[b_ptr])
                b_ptr += 1
                b_count += 1
                a_count = 0
        else:
            if b_count < k:
                c.append(b[b_ptr])
                b_ptr += 1
                b_count += 1
                a_count = 0
            else:
                c.append(a[a_ptr])
                a_ptr += 1
                a_count += 1
                b_count = 0

    print("".join(c))

t = int(input())
for _ in range(t):
    solve()