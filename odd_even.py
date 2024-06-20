# Ask the user for a number. Depending on whether the number is even or odd, print out an
# appropriate message to the user.
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Please enter your number which you want to check whether it  : "))
check = int(input("Please enter another one number : "))

if num % 2 == 0:
    print(num, "is a even number")
else:
    print(num, "is a odd number")

if num % 4 == 0:
    print(num, "is divide by number 4")
else:
    print(num, "is not divided by either 4")

if num % check == 0:
    print(num, "is divided by", check)
else:
    print(num, "is not divided by", check)



