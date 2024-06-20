# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
L1 = []

for ele in a:
    if ele in b:
        L1.append(ele)
L2 = set(L1)
print(L1)
print(L2,"are common between list a and b")

print(set([ele for ele in a if ele in b ]))