f1=open("input.txt","r")
l1=f1.readlines()
#l1.remove('Goodies and Prices:\n')
print(l1)
print()
le=len(l1)
d={}
k=l1[0][0:-1].split(":")
k=int(k[1])
print(k)
for i in range(2,le):
    if ": " in l1[i]:
        if '\n' in l1[i]:
            v=l1[i][0:-1].split(":")
        else:
            v=l1[i].split(":")
        #print(v)
        d[v[0]]=int(v[1])
d=dict(sorted(d.items(),key=lambda x:x[1]))
print(d)
le=len(d)
hl=list(d)
#print(hl)
mini=1000000
ans=-1
for kk in hl:
    print(kk,d[kk])
k=k-1
for i in range(k,le):
    x=d[hl[i]]-d[hl[i-k]]
    print(hl[i],'-->',hl[i-k],x)
    if x<mini:
        ans=i
        mini=x
f2=open('output.txt','w')
f2.write('''The goodies selected for distribution are:

''')
for i in range(ans-k,ans+1):
    ss=hl[i]+": "+str(d[hl[i]])
    f2.write(ss+"\n")
f2.write('''
And the difference between the chosen goodie with highest price and the lowest price is ''')
f2.write(str(mini))
f1.close()
f2.close()

