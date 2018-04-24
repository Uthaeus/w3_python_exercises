# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copies(s, n):
  if len(s) < 2:
    result = s * n 
  else:
    part = s[:2]
    result = part * n 

  return result

string = input("Enter a string: ")
num = int(input("How many copies? "))

print(copies(string, num))