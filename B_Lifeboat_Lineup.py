n = int(input())
rats = []
women_or_children = []
men = []
captain = ""

for _ in range(n):
    name, role = input().split()
    if role == "rat":
        rats.append(name)
    elif role == "woman" or role == "child":
        # the sam role alachewu kedmewu bimexum doesn't matter 
        women_or_children.append(name)
    elif role == "man":
        men.append(name)
    elif role == "captain":
        captain = name
order = rats + women_or_children + men
if captain:
    order.append(captain)
for name in order:
    print(name)
