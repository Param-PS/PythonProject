# List1 =[ 50, 33 , 27 , -20 , 85 , 74 , 4,9,3,7]
# Write w program which prints how many even and odd numbers are there in the above list

List1 = [50, 33, 27, -20, 85, 74, 4, 9, 3, 7]

evenNumCount = 0
oddNumCount = 0
for num in List1:
    if num%2 == 0:
        print(num, 'is a even number')
        evenNumCount += 1
    else:
        print(num, 'is a odd number')
        oddNumCount += 1
print(evenNumCount, 'even numbers are present in the list')
print(oddNumCount, 'odd numbers are present in the list')
