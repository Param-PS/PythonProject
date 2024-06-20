n = 10
n1 = 0
n2 = 1
nxtNum = n2
count = 1

while count < n:
    print(nxtNum, end=" ")
    count += 1
    n1, n2 = n2, nxtNum
    nxtNum = n1 + n2
print()

num = 11
n1, n2 = 0, 1
print("Fibonacci series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")