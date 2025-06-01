t = int(input())
mirror = {'p': 'q', 'q': 'p', 'w': 'w'}

for _ in range(t):
    a = input()
    b = ''.join(mirror[ch] for ch in reversed(a))
    print(b)
