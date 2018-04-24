# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_odd(n):
  if n % 2 == 0:
    ans = "Your number is even."
  else:
    ans = "Your number is odd."

  return ans

num = int(input("Enter a number: "))

print(even_odd(num))