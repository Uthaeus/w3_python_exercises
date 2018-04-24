# Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Enter your number: "))

def near_thousand(n):
  return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

def answer(n):
  if n >= 1900 and n <= 2100:
    return "Your number is within 100 of 2000."
  elif n >= 900 and n <= 1100:
    return "Your number is within 100 of 1000"
  else:
    return "Your number is not within 100 of either 1000 or 2000"

print(near_thousand(num))
print(answer(num))


