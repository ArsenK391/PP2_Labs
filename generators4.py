def squars(a, b):
    for i in range(a, b + 1):
        yield i * i
        
a = int(input())
b = int(input())

for square in squars(a, b):
    print(square) 