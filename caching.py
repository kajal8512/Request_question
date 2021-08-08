import os
import json
import requests

saral=requests.get('http://saral.navgurukul.org/api/courses')
res=saral.json()
with open("coures.json","w") as a:
    file=json.dump(res,a,indent=4)
path='/home/kajal/Desktop/Request in python/caching.py/coures.json'
isfile=os.path.isfile(path)
print(isfile)