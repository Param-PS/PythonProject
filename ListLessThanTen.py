# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5
# from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a
# that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newa = []

for i in a:
    if i < 5:
        print(i,"is less than 5")
        newa.append(i)
print("List that contains elements which are less than 5 is ",newa)

print("small numbers are", [ x for x in a if x < 5 ] )

num = int(input("Please enter one number : "))

L2 = []
for x in a:
    if x < num:
        L2.append(x)
        print(x,"is smaller than",num)
print(L2,"are smaller than",num)
