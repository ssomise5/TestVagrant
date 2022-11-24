import json
f=open('testData.json')
data= json.load(f)
#print(data['player'][1]['country'])
count = 0;
k=0;
while (k<len(data['player'])):
    if(data['player'][k].get('role')=="Wicket-keeper"):
        count = count+1;
    k = k+1;
#print(count)
print("TestCase 2:")
if(count==1) :
    print("Only one Wicket-Keeper is there")
    print("\n")
else:
    print("More than one Wicket-Keeper is there")
    print("\n")
f.close();