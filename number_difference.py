# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(n):
  if n > 17:
    return (n - 17) * 2
  else:
    return 17 - n 

num = int(input("Enter a number: "))
answer = difference(num)

print(answer)