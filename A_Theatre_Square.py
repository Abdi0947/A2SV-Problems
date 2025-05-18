import math
n, m, a = map(int, input().split())

flagstones_x = math.ceil(n / a)
flagstones_y = math.ceil(m / a)

# Total flagstones
total_flagstones = flagstones_x * flagstones_y

print(total_flagstones)
