import operator
nums=[5,2,0,3,1]

arr=[]
arr.append(nums[0])
for i in range(1,len(nums)):
    result=0
    for val in arr:
        result^=val
    b=operator.xor(result,nums[i])
    arr.append(b)
print(arr)