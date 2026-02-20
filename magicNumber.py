def isMagic(n):
    s = 0
    while (n > 0 or s > 9):
        if n == 0:
            n = s
            s = 0
        s = s + n % 10
        n = n // 10
    return s == 1


nums = list(map(int,input("Enter num in list").split()))
for num in nums:
    if (isMagic(num)):
        print(f"{num} magic number")
    else:
        print(f"{num} not a magic number")
