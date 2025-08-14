nums = [-6,2,5,-2,-7,-1,3]
target = -2
count=0
for j in range(len(nums)):
    print(j)
    for i in range(j):
        print(i)
        if((nums[i]+nums[j])<target):
           
            
            count+=1
print(count)
