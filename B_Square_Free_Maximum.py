import math
n = int(input())
a = list(map(int, input().split()))
les=-10**7
for num in a:
    if num<0 or math.sqrt(num)**2 != num:
       les=max(les,num)
print(les)