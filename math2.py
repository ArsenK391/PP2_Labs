def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = int(input())
base1 = int(input())
base2 = int(input())

area = trapezoid_area(height, base1, base2)
print(area) 