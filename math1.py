import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = int(input())
radians = degrees_to_radians(degrees)
print(radians) 