# Write a Python program to get the volume of a sphere with radius 6.
# V=(4/3)*pi*(r**3)
from math import pi

radius = float(input("Enter a radius: "))

def sphere_volume(r):
  return (4 / 3) * pi * (r ** 3)

answer = sphere_volume(radius)

print("The volume of a sphere with a radius of " + str(radius) + " is: ", answer)