# for i in range(1, 30):
#     if i == 1:
#         print(i, 'is not a prime number')
#     elif i > 1:
#         for x in range(2, i):
#             if i % x == 0:
#                 break
#         else:
#             print(i, ' is a prime number')

for n in range(1, 101):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if n % i == 0:
                status = False

        if status:
            print(n, '', sep=',', end='')