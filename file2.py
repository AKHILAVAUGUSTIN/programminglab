a=open("doc.txt","r")
b=open("do.txt","w")
c=a.readlines()
d=len(c)
for i in range(0,d):
 if(i%2==0):
     b.write(c[i])
 else:
     pass
b.close()
b=open("do.txt","r")
e=b.read()
print(e)
a.close()
b.close()