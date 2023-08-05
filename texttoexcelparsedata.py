import pandas as pd 
import re
def read_file():
    with open('C:\\Users\\DELL\\Documents\\Delhi CIoT vMME_0305_865_Fail and Succ.txt', 'r') as f:
        readfile = f.read()
    return readfile
usedwords = []
data1=[] 
data2 = []
data = read_file() 
#spilt the line based on semicolon;  
words=(data.split(';'))
for word in words:
    if re.search('='*5, word):
        usedwords.append(word)
#Count '=' value and append key and value in array
for word in usedwords:
    count = word.count('=')
    data1.append(word.split('='*(count-1))[1])  
keys = usedwords[0].split('='*(count-1))[0]
keys = keys.replace('RESULT','')
keys = keys.replace('=','')
keys = keys.replace('OK','')
keys = re.sub(r"\s+", ';', keys)[1:-1]
#Remove the  blanks space from left and right value from string
for fi in data1:
    data2.append(re.sub(r"\s+", ';', fi)[1:-1].split(';'))
#Create dictionary to store string value
d = {k:[] for k in keys.split(';')}
countofcoulmn = len(d)
for value in data2:
    for i,j in zip(value,d.keys()):
        if len(i)<50 and re.search(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}",i):
            d[j].append(i+" "+value[value.index(i)+1])
            value.remove(value[value.index(i)+1])
        elif len(i)<50 :
            d[j].append(i) 
df = pd.DataFrame(d)
df.pop("DIR") 
df = df.rename(columns={"INDEX":"ID"})
df.to_csv('C:\\Users\\DELL\\Documents\\test.csv', index=False)




