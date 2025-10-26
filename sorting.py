names = ["Mary","John","Emma"]
heights = [180,165,170]
ha=[]
for i in range(len(heights)):
    ha.append(i)
print(ha)
        
for i in range(len(heights)-1):
    for j in range(i+1,len(heights)):
        if(heights[j]>heights[i]):
            temp=heights[j]
            heights[j]=heights[i]
            heights[i]=temp
            new=ha[j]
            ha[j]=ha[i]
            ha[i]=new
print(ha)
print(heights)
result=[]
for i in range(len(ha)):
    names[i]=names[ha[i]]
print(names)