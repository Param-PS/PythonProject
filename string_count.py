name = "Paramasivan"

fav = set(name)
print("Converted set is ", fav)

for x in fav:
    print(x,"count is : ", name.count(x))


res = {i: name.count(i) for i in set(name)}
print(type(res))
print(res)
fina = str(res)
print(type(fina))
print(str(res))
