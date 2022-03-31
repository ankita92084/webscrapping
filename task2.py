import json
file=open("top_movie.json","r")
a=file.read()
# loads=its convert json string into pytho object
data=json.loads(a)
i=0
while i<len(data):
    j=0
    while j<len(data):
        if data[i]["year"] < data[j]["year"]:
            d=data[i]
            data[i]=data[j]
            data[j]=d
        j+=1
    i+=1
dict1 = {}
i = 0
while i < len(data):
    list = []
    j = 0
    while j < len(data):
        if data[i]["year"] == data[j]["year"]:
            list.append(data[j])
        j+=1
    dict1[data[i]["year"]] = list
    i+=1
with open("group_by_year.json","w") as f:
# dumb its works to write
    json.dump(dict1 , f , indent=4)
    