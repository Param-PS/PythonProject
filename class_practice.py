class myCar():
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def display(self):
        print("Name of the car is", self.name)
        print("Brand of the car is", self.brand)

i20 = myCar("i20", "Hyundai")
audi = myCar("Q5", "Audi")

print("Car name is", i20.name)
print("Brand name is", audi.brand)
i20.display()
audi.display()
