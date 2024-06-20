import json

f = open('C:/Users/paramasivan.d/PycharmProjects/pythonProject/example_2.json')

data = json.load(f)

for i in data["quiz"]["maths"]["q2"]:
    print(i)

f.close()