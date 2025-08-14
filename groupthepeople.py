groupSizes = [3,3,3,3,3,1,3]
groups={}
result=[]
for person,size in enumerate(groupSizes):
    if(size not in groups):
        groups[size]=[]
    groups[size].append(person)
    if(len(groups[size])==size):
        result.append(groups[size])
        groups[size]=[]
print(result)
