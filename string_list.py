# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

text = str(input("Please enter some word : ")).lower()

text_rev = text[::-1]
print(text_rev)

if text == text_rev:
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")
