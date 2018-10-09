t=int(input())
while t!=0:
    p=int(input())
    x=[0,1]
    sum1=0
    for i in range(p-1):
        x.append(x[i]+x[i+1])
        print(x[i],end=" ")
        sum1=sum1+x[2*i+1]
        print(sum1)
