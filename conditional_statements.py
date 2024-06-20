a = 336
b = 335

if a > b:
    print(a, "is greater than", b)
elif a == b:
    print(a, "and", b, "are equal")
else:
    print(a, "is smaller than", b)

print(a, "is greater") if a > b else print(a, "and", b, "are equal") if a == b else print(a, "is smaller")

