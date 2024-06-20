import json
fvar = open(r'C:\Users\paramasivan.d\PycharmProjects\pythonProject\example_1.json', 'r')
jdata = json.load(fvar)
fvar.close()

fruit = jdata['fruit']
print(fruit)

fvar1 = open(r'C:\Users\paramasivan.d\PycharmProjects\pythonProject\example_2.json', 'r')
jdata1 = json.load(fvar1)
fvar1.close()

ans = jdata1['quiz']['sport']['q1']['answer']
print(ans)

fvar = open(r'C:\Users\paramasivan.d\PycharmProjects\pythonProject\example_2.json', 'r')
jsdata = json.load(fvar)
fvar.close()
