n = int(input())
while n!=0:
    s = input()
    if len(s)<11:
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])
    n-=1
