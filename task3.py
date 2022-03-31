import json
file = open("group_by_year.json","r")
a = file.read()
# loads its convert python object into json string
data = json.loads(a)
dict1={}
for i in data:
    list1=[]
    a=str(i)
    for j in data:
        b=str(j)
        # print(b)
        if a[:3]==b[:3]:
# its check our number till 3
            k=0
            while k<len(data[j]):
                if data[j][k] not in list1:
                    list1.append(data[j][k])
                k+=1
    b=a[:3]+"0"
    dict1[int(b)]=list1                    
with open("group_by_decade.json","w") as f:
        json.dump(dict1,f,indent=4)