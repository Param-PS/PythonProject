name = "Hello World!!"
# count = len(name)
# for i in (len/2):
#
# res = name.reverse()
# print(res)

revname = name[::-1]
print(revname)

str1 = ''
for i in name:
     str1 = i + str1
print('Original string is : ', name)
print('Reversed string is : ', str1)
