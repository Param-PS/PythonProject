fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
print(fruits[0])
print(len(fruits))
print(type(fruits))

# list() constructor
cars = list(("i20", "Virtus", "Creta", "Slavia", "Fronx", "XUV700", "Venue", "Seltos", "Sonet"))
print(cars)

# Accessing list items
#   - Positive indexing
#   - Negative indexing
#   - Range of indexes
# Positive indexing
print(cars[3])

# Negative indexing
print(cars[-1])

# Range of indexes
print(cars[2:5])
print(cars[:3])
print(cars[3:])
print(cars[-4:-1])
print(cars[-4:])
print(cars[:-1])

# Check item exists or not

if "i20" in cars:
    print("yes!!! i20 is there in cars list")
else:
    print("No!!! i20 is not there in cars list")

# Change list item value

cars = list(("i20", "Virtus", "Creta", "Slavia", "Fronx", "XUV700", "Venue", "Seltos", "Sonet"))

cars[4] = "Nexon"
print(cars)

cars[3:6] = ["Octavia", "S-Cross", "Thar"]
print(cars)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)



# Add list items
#   1. append()
#   2. insert()
#   3. extend() - To append another list or other iterables to current list

# append()
thislist.append("Guava")
print(thislist)

# Insert iterms
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("Kiwi", "Orange")
thislist.extend(thistuple)
print(thislist)

# Remove specific Item
#   1. remove()
#   2. pop()
#   3. del
#   4. clear()

# remove()
thislist.remove("banana")
print(thislist)

# pop() - Removes specified index item
thislist.pop(2)
print(thislist)

thislist.pop()
print(thislist)

# del - Keyword removes the specified index
del thislist[1]
print(thislist)

# clear() - removes all items in list and remains empty list

thislist.clear()
print(thislist)

del thislist  # To delete the list

# Loop through a list
#   1. for
#   2. loop through index number using range() and len()
#   3. while
#   4. List comprehension

# for
cars = list(("i20", "Virtus", "Creta", "Slavia", "Fronx", "XUV700", "Venue", "Seltos", "Sonet"))
for item in cars:
    print(item)

# loop through index number using range() and len()
for item in range(len(cars)):
    print(item)
    print(cars[item])

# while

i = 0
while i < len(cars):
    print(cars[i])
    i += 1

# List comprehension

[print(x) for x in cars]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for fru in fruits:
    if "a" in fru:
        newlist.append(fru)
print(newlist)

newlist = [fru for fru in fruits if "a" in fru]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist.reverse()
print(thislist)

# Copy list
#   - copy()
#   - list(listname)

a = ["i20", "venue", "creta"]
b = ["sonet", "seltos", "carens"]
c = a.copy()
d = list(b)

print(c)
print(d)

# Join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# List methods
#   - append()
#   - clear()
#   - copy()
#   - count()
#   - extend()
#   - index()
#   - insert()
#   - pop()
#   - remove()
#   - reverse()
#   - sort()
