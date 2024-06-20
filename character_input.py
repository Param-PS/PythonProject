# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
year = (2024 + 100) - age
print("Dear", name, "you will be 100 years old in the year", year)