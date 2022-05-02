a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))


def triangle_sort(a: int, b: int, c: int):
    sides = [a, b, c]
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:

        if a == b & b == c:
            return "Equilateral triangle"
        elif a == b | b == c:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"

    else:
        return "This is not a triangle."


classification = triangle_sort(a, b, c)
print(classification)
