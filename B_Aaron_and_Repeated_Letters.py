string=input()
arr=[]
for letter in string:
    if len(arr)!=0 and arr[-1]==letter:
        arr.pop()
    else:
        arr.append(letter)
print(''.join(arr))