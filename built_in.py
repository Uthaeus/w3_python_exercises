# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
# Sample function : abs()
# Expected Result : 
# abs(number) -> number

n = int(input("Enter a number: "))

def abs(number):
  if number < 0:
    return number * -1
  else:
    return number


print("abs(number): -> ", abs(n))

