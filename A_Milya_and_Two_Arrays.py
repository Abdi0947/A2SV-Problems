t = int(input())  
for _ in range(t):  
        n = int(input())  
        a = list(map(int, input().split()))  
        b = list(map(int, input().split()))  
        yourset = set() 

        for i in range(n):
            for j in range(len(a)):
                if b[i] + a[j] not in yourset:
                    yourset.add(b[i] + a[j])

        if len(yourset) >= 3:
            print("YES")
        else:
            print("NO")
            # 3 4 2.....b
            # 1 5 6...a
            
