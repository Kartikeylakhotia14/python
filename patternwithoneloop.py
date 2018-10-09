j=6
k=j
l=1
for i in range(1,13,1):
    if i>6:
       l=12-i;
    else:
        l=i
    print(k*" "+l*"* ")
    j=j-1;
    k=abs(j)
    if i==5 :
       j=-1
    
