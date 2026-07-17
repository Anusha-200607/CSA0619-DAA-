def social_media_processing(n):
    if n == 1:
        return 1
    return social_media_processing(n - 1) + n

n = int(input("Enter number of posts: "))

result = social_media_processing(n)

print("Total Processing Cost =", result)
