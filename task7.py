import json
def  movie_directors():
    file2=open("my_file_5.json","r")
    h=json.load(file2)
    # print(y)
    list=[]
    for i in h:
        # print(y)
        # print(i["Original Language"])
        if i["Director:"]not in list:
            list.append(i["Director:"])
    dict8={}
    list9=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["Director:"]:
                count+=1
            i+=1
        dict8.update({k:count})
    list.append(dict8)
    with open("task_7.json","w")as file:
        json.dump(dict8,file,indent=4)
    return dict8
movie_directors()



