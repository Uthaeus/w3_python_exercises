# Write a Python program to print the following string in a specific format (see the output)

l_one = 'Twinkle, twinkle, little star,'
l_two = 'How I wonder what you are!'
l_three = 'Up above the world so high,'
l_four = 'Like a diamond in the sky.'

# space = ' '

# print(l_one)
# print((space * 25) + l_two)
# print((space * 50) + l_three)
# print((space * 50) + l_four)
# print((space * 25) + l_two)
# print(l_one)

content = """
Twinkle, Twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are.
"""

print(content)