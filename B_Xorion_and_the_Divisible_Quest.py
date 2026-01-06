n = int(input())
a = list(map(int, input().split()))

min_val = min(a)

# if all(x % min_val == 0 for x in a):
#     print(min_val)
# else:
#     print(-1)
isno = True
for num in a:
    if num % min_val != 0:
        isno=False
        break
print(min_val if isno else -1)