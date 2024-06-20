msg = "Welcome to Python Tutorial"
print(msg)
print("*********************")
multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_string)
print("*********************")

print(msg[1])
print("Length of the msg variable string is ", len(msg))
for val in msg:
    print("Character in msg variable is ", val)

print("Python" in msg)
if "python" in msg:
    print("Key word Python is present in msg")
elif "Python" not in msg:
    print("Key word not present in multiline_string also")
else:
    print("Key word python is not present in msg")

# String slicing

b = "Hello World!"

print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-1])

# Modify operations
# upper() - returns the string in upper case
# lower() - returns the string in lower case
# strip() - removes any whitespace from the beginning or the end
# replace() - replaces a string with another string
# split() - splits the string into substrings if it finds instances of the separator

print("Upper case of variable b is ", b.upper())
print("Lower case of variable b is ", b.lower())

# strip()
b = " Hello, World! "
print("String before doing strip operation is ", b)
print("String after doing strip operation is ", b.strip())

# replace()
b = "Hello World!"
print(b.replace("o", "x"))
print(b)

# split()
b = "Hello, World!"
print(b.split(","))

# String Concatenation
fname = "Sagar"
lname = "Birla"

print(fname + lname)
print(fname+" "+lname)

# Format string
# format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.
age = 31
txt = "My name is Ram, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 499.50
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))

# Escape character
txt = "We are the so-called \"vikings\" from the north."
print(txt)

# String methods
# capitalize() - Converts the first character to upper case
# casefold() - Converts string into lower case
# center() - It will center align the string, using a specified character (space is default) as the fill character.
# count() - Returns the number of times a specified value occurs in a string
# encode() - Returns an encoded version of the string
# endswith() - Returns true if the string ends with the specified value
# expandtabs() - Sets the tab size of the string
# find() - Searches the string for a specified value and returns the position of where it was found
# format() - Formats specified values in a string
# index() - Searches the string for a specified value and returns the position of where it was found
# isalnum() - Returns true if all characters in the string are alphanumeric
# isalpha() - Returns True if all characters in the string are in the alphabet
# join() - Joins the elements of an iterable to the end of the string
# lstrip() - Remove spaces to the left of the string
# maketrans() - Returns a mapping table that can be used with the translate() method to replace specified characters.
# partition() - Returns a tuple where the string is parted into three parts based on the given string
# swapcase() - Swaps cases, lower case becomes upper case and vice versa
# title() - Converts the first character of each word to upper case

name = "Dheeran Chinna malai"

print(name.capitalize())
print(name.casefold())
print(name.center(50))
print(name.center(50, "*"))
print(name.count("a"))
print(name.encode())
print(name.endswith("lai"))

txt = "H\te\tl\tl\to\t"
print(txt.expandtabs(2))

print(name.find("a"))
print(name.find("z"))

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# index() and find() are similar. Only difference is find() will not return error if the searched character not found.
print(name.index("a"))
# print(name.index("z"))

id = "Adhit21"
print("Given id is alpha numeric:", id.isalnum())
print("Given id has only alphabet:", id.isalpha())

# join()
fruits = ["Apple", "Orange", "Cherry"]
my_choice = ",".join(fruits)
print(my_choice)

# lstrip()
txt = "   Banana   "
print(txt.lstrip())

txt = ",,,..sasw banana"
print(txt.lstrip(",. asw"))

# maketrans()
txt = "Hello Jem!"
repl = str.maketrans("J", "G")
print(txt.translate(repl))

# partition()
txt = 'I am a farmer and cultivated banana'
print(txt.partition("and"))

# swapcase()
txt = "I am a Farmer and cultivated Banana"
print(txt.swapcase())

# title()
txt = "man of the match in this series"
print(txt.title())