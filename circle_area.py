# Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi 

def circle(r):
  return (r ** 2) * pi

radius = float(input("What is the radius?\n"))

print("The area of the circle is:")
print(circle(radius))
