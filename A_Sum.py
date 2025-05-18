n = int(input())  # Number of test cases

for _ in range(n):
    nums = list(map(int, input().split()))  # Read the list of integers
    found = False  # Flag to track if the condition is met
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:  # Ensure we don't use the same index
                target = nums[i] + nums[j]
                if target in nums and nums.index(target) != i and nums.index(target) != j:
                    print("YES")
                    found = True
                    break
        if found:
            break
    if not found:
        print("NO")
