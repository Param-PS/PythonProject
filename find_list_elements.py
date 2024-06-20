# 5. L1 = ["python is good" , "Java is ok" , "i love python" , "c is mother lang" , "python rocks"]
# please print all the elements of the list which has word python present in it and count how many elements contsins python word

L1 = ["python is good", "Java is ok", "i love python", "c is mother lang", "python rocks"]

count = 0

for i in L1:
    if 'python' in i:
        print(i + ' contains word python')
        count += 1
print('Word python present', count, 'times in the list')

