n=int(input())
for i in range(10000,1000000):
    sum=0
    j=i
    strj=str(j)
    if strj==strj[::-1]:
        while i!=0:
            sum+=i%10
            i=(int)(i/10)
        if sum==n:
         #strj=str(j)
         #if strj==strj[::-1]:
            print(j)
