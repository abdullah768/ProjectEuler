x=1
val=1
for i in range (1,501):
    for j in range (1,5):
        val=val+2*i
        x=val+x
    print(val)
print(x)
