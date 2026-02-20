def rectangle(l, b):
    return 2 * (l + b)


def circle(r):
    return 2 * 3.14 * r


def square(s):
    return 4 * s


def triangle(a, b, c):
    return a + b + c


a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
r = int(input("r="))
s = int(input("s="))
l = int(input("l="))

square(s)
rectangle(l, b)
circle(r)
triangle(a, b, c)

print(f"area of square = {square(s)}")
print(f"area of rectangle = {rectangle(l, b)}")
print(f"area of circle = {circle(r)}")
print(f"area of triangle = {triangle(a, b, c)}")
