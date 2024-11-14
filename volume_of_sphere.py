import math

def calculate_volume_of_sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = 30
print(calculate_volume_of_sphere(radius))

radius = 40
print(calculate_volume_of_sphere(radius))