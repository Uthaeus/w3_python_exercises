# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copies(s, n):
  return (s + "\n") * n 

sentence = input("Enter a sentence:\n")
times = int(input("How many copies do you want? "))

print(copies(sentence, times))