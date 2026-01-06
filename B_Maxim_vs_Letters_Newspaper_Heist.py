from collections import Counter

s1 = input().rstrip("\n")   
s2 = input().rstrip("\n")   
letter = Counter(ch for ch in s1 if ch != ' ')
for ch in s2:
    if ch == ' ':  
        continue
    if letter[ch] == 0:  
        print("NO")
        break
    letter[ch] -= 1      
else:
    print("YES")   
