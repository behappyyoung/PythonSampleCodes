from sys import argv
import json

script, filename, savefile = argv

with open(filename) as data_file:
	data = json.load(data_file)

newlist =[]
appType =[]
for s in data['Result']['AppTemplates']['Results']:
    apptype = s['Row']['WebAppType']
	
    newlist.append({'ID':s['Row']['ID'], 'Type': apptype, 'DisplayName': s['Row']['DisplayName'], 'Category':s['Row']['Category'], 'Icon':'https://cloud.centrify.com' + s['Row']['Icon'], 'Desc':s['Row']['Description']})
    
    if apptype in appType:
        continue        
    else:
        appType.append(apptype)

newDic={}
newDic['categories'] = data['Result']['Categories']
newDic['apps'] = newlist
newDic['apptype'] = appType
with open(savefile, 'w+') as fp:
	json.dump(newDic, fp)
