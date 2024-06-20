reqnum = int(input("Please enter the number which you want to calculate : "))

n1 = 0
n2 = 1
n3 = n2
count = 0

if reqnum <= 0:
    print("Please enter the positive number")
elif reqnum == 1:
    print("Fibonacci sequence upto", reqnum, ":", n1)
else:
    print("Fibonacci sequence upto", reqnum, ":")
    while count <= reqnum:
        print(n3)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
