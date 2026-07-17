def authentication(n):
    if n <= 1:
        return 1
    return authentication(n // 2) + 1

n = int(input("Enter authentication size: "))

result = authentication(n)

print("Verification Levels =", result)
