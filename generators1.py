def square_generator(N):
    for i in range(N + 1):
        yield i * i
        
N = int(input())
for square in square_generator(N):
    print(square)
