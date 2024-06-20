import csv

filename = "C:/Users/paramasivan.d/PycharmProjects/pythonProject/EDAServiceUsers.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(type(csvreader))

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

print('Field names are:' + ', '.join(field for field in fields))

for row in rows:
    for ele in row:
        print(ele, end=",")
    print('\n')
