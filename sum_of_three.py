# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

def summer(n1, n2, n3):
  if n1 == n2 and n2 == n3:
    return (n1 + n2 + n3) * 3
  else:
    return n1 + n2 + n3

def thrice(n1, n2, n3):
  sum = n1 + n2 + n3 

  if n1 == n2 == n3:
    sum = sum * 3

  return sum

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print(summer(num1, num2, num3))
print(thrice(num1, num2, num3))

 
