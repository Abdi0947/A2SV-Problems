n = int(input())
ratings = list(map(int, input().split()))
positions = []
for rating in ratings:
    count = 0
    for other in ratings:
        if other > rating:
            count += 1
    positions.append(str(count + 1))
print(' '.join(positions))