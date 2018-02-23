pre=[set() for i in range(10)]
pos=[set() for i in range(10)]
for i in range(50):
    n=input();
    a=int(n[0])
    b=int(n[1])
    c=int(n[2])
    pos[a].add(b);
    pos[a].add(c);
    pos[b].add(c)
    pre[b].add(a);
    pre[c].add(b)
    pre[c].add(a)
for i in range (10):
    print(pre[i],i,pos[i],sep=' ')
