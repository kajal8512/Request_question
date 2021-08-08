import json
import requests
import os 
# import pprint
if os.path.isfile("coures.json"):
    # r=requests.get('http://saral.navgurukul.org/api/courses')
    with open("coures.json","r") as a:
        res=json.load(a)
else:
    r=requests.get('http://saral.navgurukul.org/api/courses')
    res=r.json()
    with open("coures.json","w") as b:
        json.dump(res,b,indent=4)

k=1   
for i in res.values():
    for x in i:
        print(k,x["name"],"ID:",x["id"])
        k+=1
user=int(input("enter courses no."))
print("")
if os.path.isfile("parent.json"):
    # user=int(input("enter courses no."))
    # print("")
    with open("parent.json","r") as b:
        cou=json.load(b)
else:
    user=int(input("enter courses no."))
    coures=requests.get('http://saral.navgurukul.org/api/courses/'+str(res["availableCourses"][user-1]["id"])+'/exercises')
    cou=coures.json()
    print("")
    with open("parent.json","w") as b:
        json.dump(cou,b,indent=4)        
s=1  
for t in cou.values():
    for y in t:
        print(s,y["name"])
        s+=1
           
z=0
user1=int(input("enter parent no."))   
if cou["data"][user1-1]["childExercises"]!=[]:
    for y in range(len(cou["data"][user1-1]["childExercises"])):
        print(z,cou["data"][user1-1]["childExercises"][y]["name"])
        z+=1
    child=int(input("Enter the child no."))
    # print(cou["data"][user1-1]["childExercises"][child-1]["slug"])
    # print(cou["data"][user1-1]["childExercises"][child-1]["id"])
    # print(que[res])
    question=requests.get('http://saral.navgurukul.org/api/courses/'+str(cou["data"][user1-1]["childExercises"][child-1]["id"])+'/exercise/getBySlug?slug='+cou["data"][user1-1]["childExercises"][child-1]["slug"])
    l=('http://saral.navgurukul.org/api/courses/'+str(cou["data"][user1-1]["childExercises"][child-1]["id"])+'/exercise/getBySlug?slug='+cou["data"][user1-1]["childExercises"][child-1]["slug"]+'')
    print(l)
    que=question.json()
    with open("slug.json","w") as k:
        json.dump(que,k,indent=4)
    
    print(que["content"])
else:
    print(cou["data"][user1-1]["slug"])
        