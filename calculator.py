# 3. write a prog for calculator
#
# take 3 inputs from user
#
# 1st input = operation(add , sub , mul , div)
# 2nd input = number
# 3rd input = number
#
#
# add = input2 + input3
# sub = inpur2 - input3
# mul = inpur2 * input3
# div = inpur2 / input3
#
# if any other operation other than add , sub , mul , div u need to print invalid operation

print("Calculator operator accepted are +, -, * or /")
oper = input("Please enter the operator = ")
if oper not in ['+', '-', '*', '/']:
    print("Invalid operator", oper, "Please select valid operator")
    exit()

num1 = int(input("enter the first number = "))
num2 = int(input("enter the second number = "))

if oper == "+":
    res = num1 + num2
    print("Sum of ", num1, "and", num2," is ", res)
elif oper == "-":
    res = num1 - num2
    print("Subtract of ", num1, "and", num2," is ", res)
elif oper == "*":
    res = num1 * num2
    print("Multiplication of ", num1, "and", num2," is ", res)
elif oper == "/":
    res = num1 / num2
    print("Divide of ", num1, "and", num2," is ", res)
else:
    print("Invalid operator", oper, "accepted operators are +, -, * and /")

