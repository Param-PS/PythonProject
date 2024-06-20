thisdict = {
    "Name": "Param",
    "Age": 32,
    "Mobile": 8892223883,
    "weight": 67.400
}
print(thisdict)

print(len(thisdict))
print(type(thisdict))

vw_car = dict(Name = "Polo", Model = 2020, country = "Germany", color = ["White", "Red", "Silver", "Blue"])
print(vw_car)

# Access dictionary items
# dict name and key
# get()
# keys()
# values()
# items()

print(vw_car["Name"])
print(vw_car.get("Model"))
print(vw_car.keys())
print(vw_car.values())

vw_car["Model"] = 2021
print(vw_car)

vw_car["Owner"] = "S.P.Nalan Adhit"
print(vw_car)

x = vw_car.items()
print(x)

# change item in dictionary

thisdict.update({"year": 1992})
print(thisdict)