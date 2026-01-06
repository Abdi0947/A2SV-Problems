import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(0)
        return
    total_sq_sum = sum(x**2 for x in a) + sum(x**2 for x in b)
    total_sum = sum(a) + sum(b)
    max_possible_sum = 100 * n + 1
    dp = [False] * max_possible_sum
    dp[0] = True
    current_limit = 0
    for i in range(n):
        new_dp = [False] * max_possible_sum
        val_a = a[i]
        val_b = b[i]
        for s in range(current_limit + 1):
            if dp[s]:
                new_dp[s + val_a] = True
                new_dp[s + val_b] = True
        dp = new_dp
        current_limit += max(val_a, val_b)
    min_sq_sum_of_totals = float('inf')
    for s_a in range(max_possible_sum):
        if dp[s_a]:
            s_b = total_sum - s_a
            min_sq_sum_of_totals = min(min_sq_sum_of_totals, s_a**2 + s_b**2)
            
    ans = (n - 2) * total_sq_sum + min_sq_sum_of_totals
    print(ans)

def main():
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line)
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()