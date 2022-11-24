import json
f=open('testData.json')
data= json.load(f)
#print(data['player'][1]['country'])
count = 0;
k=0;
while (k<len(data['player'])):
    if(data['player'][k].get('country')!="India"):
        count = count+1;
    k = k+1;
print("TestCase1:")
print("Total Number of Foreign Players:", count)
print("\n")
f.close();