class Kar():
    global num
    num = 0
    def myfunc(self):
        global num
        num = 15
        print(num)
    def myfunc2(self):
        print(num)

obj = Kar()
obj.myfunc()
obj.myfunc2()