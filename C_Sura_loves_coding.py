originalWord = []
n = int(input())
s = input().strip()

for i in range(n - 1, -1, -1):
    originalWord.insert(len(originalWord) // 2, s[i])

print(''.join(originalWord))
