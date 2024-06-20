msg = "Hello World!!"

rev_msg = ""

for letter in msg:
    rev_msg = letter + rev_msg

print("Reversed string is:", rev_msg)

print(msg[::-1])

fruits = ["apple", "banana", "orange", "mango"]
k= len(fruits) - 1
L2 = []
for i in range(k, -1, -1):
    p = fruits[i]
    L2.append(p)
print("Actual list is:", fruits)
print("Revered list is:", L2)