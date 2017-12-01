m=0
for i in range(1,100):
    for j in range(1,100):
        t=sum([int(char) for char in str(i**j)])
        if(t>m):
            m=t
print(m)
