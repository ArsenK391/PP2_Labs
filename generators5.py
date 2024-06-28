def countdouwn(n):
    for i in range(n, -1, -1):
        yield i
        
n = int(input())
for number in countdouwn(n):
    print(number) 