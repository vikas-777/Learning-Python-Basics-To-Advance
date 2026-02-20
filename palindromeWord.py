def pal(s):
    s = s.upper()
    if s == s[::-1]:
        return f"{s} is palindrome"
    else:
        return f"{s} not a palindrome"
print(pal("racecar"))
