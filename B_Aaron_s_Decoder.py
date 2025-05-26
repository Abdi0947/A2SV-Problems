t = int(input())  # Read the number of test cases
for _ in range(t):
    n = int(input())  # Read the length of the binary strings
    a = input()  # Read the binary string a
    b = input()  # Read the binary string b

    # A flag that tracks if it's possible to make all 1's in a turn to 0's
    can_swap = False
    possible = True
    
    # Iterate through the string from the second character to the end
    for i in range(n):
        if a[i] == '1':
            # If we encounter '1' in a, we need to check if we have enough swaps available
            if not can_swap:
                possible = False
                break
        # If we encounter '1' in both a[i] and b[i], we know we can perform a swap
        if a[i] == '1' and b[i] == '1':
            can_swap = True
    
    print("YES" if possible else "NO")
