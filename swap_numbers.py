x = 5
y = 10
print("value of x before swapping:",x)
print("value of y before swapping:",y)

x, y = y, x

print("value of x after swapping:",x)
print("value of y after swapping:",y)

a = 0
b = 1
c = 15
print("fibanacci series:", a, b, end=" ")
for i in range(2, c):
    d = a + b
    a = b
    b = d
    print(d, end=" ")