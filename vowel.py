# Write a Python program to test whether a passed letter is a vowel or not.

def vowel(l):
  vowels = ['a', 'e', 'i', 'o', 'u']

  if l == 'y':
    result = "Your letter is sometimes a vowel ;)"
  elif l in vowels:
    result = "Your letter is a vowel."
  else:
    result = "Your letter is a consonant."

  return result

letter = input("Enter a letter: ").lower()

print(vowel(letter))