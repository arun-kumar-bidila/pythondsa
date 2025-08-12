nums=[1,2,3,4,5,6,7,8,91,4,5,6,7]
result={}
for i in range(0,len(nums)-1):
    if(nums[i] in result):
        result[nums[i]]+=1
    
    else:
        result[nums[i]]=1
print(result)