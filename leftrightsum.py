nums = [10,4,8,3]
leftsum=[]
rightsum=[]
for i in range(len(nums)):
    leftsumvalue=sum(nums[:i])
    rightsumvalue=sum(nums[i+1:])
    leftsum.append(leftsumvalue)
    rightsum.append(rightsumvalue)
answer=[]
print(leftsum)
print(rightsum)
for i in range(len(nums)):
    diff=abs(leftsum[i]-rightsum[i])
    answer.append(diff)
print(answer)