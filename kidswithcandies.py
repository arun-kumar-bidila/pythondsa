candies = [2,3,5,1,3]
extraCandies = 3
result=[]
for i in range(0,len(candies)):
    if(candies[i]+extraCandies>=max(candies)):
        result.append(True)
    else:
        result.append(False)
print(result)