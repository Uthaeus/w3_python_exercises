# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

def compute(n):
  b = n + n 
  c = n + n + n 
  return int(n) + int(b) + int(c)


number = input("Enter a number: ")

print(compute(number))