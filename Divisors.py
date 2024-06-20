# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Enter your number : "))

L1 = range(1, num+1)
L2 = []

for i in L1:
    if num % i == 0:
        print(num,"is divisible by",i)
        L2.append(i)
print(L2,"are the divisors of",num)
