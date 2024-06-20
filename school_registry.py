# 2. Write a program for the school registry example
# please take total marks as input from user for max 600
# calculate the percentage of the total marks and verify if the student has passed in which grade
#
# >=0 and  <35    ----> FAIL
# >=35 and < 50   ====> passed in third class
# >=50 and < 60  ====> passed in second class
# >=60 and <85 ====> passed in first class
# >=85 and <= 100  ==> distinction
# apart above any other percentage comes its invalid entry

maxMark = 600

studMark = int(input("Please enter the student's total mark = "))

per = (studMark/maxMark)*100
print("Student got ", per, "%")

if per >= 0 and per < 35:
    print("FAIL")
elif per >= 35 and per < 50:
    print("Passed in third class")
elif per >= 50 and per < 60:
    print("Passed in second class")
elif per >= 60 and per < 85:
    print("Passed in first class")
else:
    print("Distinction")
