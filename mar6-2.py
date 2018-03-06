import json


def readFile(filename):
    filehandler = open(filename, "r")
    filecontent = filehandler.read()
    print(filecontent)
    filehandler.close()
    return filecontent


def stuff(content):
    jsooon = json.loads(content)
    print('name' + "\t" + 'address' + "\t" + "\t" + 'city' + "\t" + "\t"+  'state' + "\t" + 'principal')
    print(jsooon['name']+ '\t' + jsooon['address'] + '\t' + jsooon['city'] + '\t' + jsooon['state']+ '\t' + jsooon['principal'])


filestuff = readFile('mar6.json')
stuff(filestuff)
