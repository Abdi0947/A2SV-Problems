c=int(input())
for i in range(c):
    c=int(input())
    if 1900<=c:
        print("Division 1")
    elif 1600<=c<=1899:
        print("Division 2")
    elif 1400<=c<=1599:
        print("Division 3")
    else :
        print("Division 4")
