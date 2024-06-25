def even_number_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
            
n = int(input())
even_numbers = list(even_number_generator(n))
print(", ".join(map(str, even_numbers)))
