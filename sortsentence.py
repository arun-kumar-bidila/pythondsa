s= "is2 sentence4 This1 a3"
news=s.split()
print(news)
result={}
for word in news:
    result[(int(word[-1])-1)]=word[0:len(word)-1]
print(result)
some=""
for i in range(len(news)):
    some+=result[i]
    some+=" "
print(some)
