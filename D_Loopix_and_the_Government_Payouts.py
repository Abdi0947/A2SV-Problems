n = int(input())
balances = list(map(int, input().split()))
q = int(input())

max_payout = 0  # track the highest government payout

for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        p, x = event[1]-1, event[2]
        # Apply max_payout from previous payouts
        balances[p] = max(x, max_payout)
    else:
        x = event[1]
        max_payout = max(max_payout, x)

# Apply any remaining government payout to all citizens
for i in range(n):
    balances[i] = max(balances[i], max_payout)

print(*balances)
