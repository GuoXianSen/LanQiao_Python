for i in range(1000,10000):
    j=i
    strj=str(j)
    if(strj==strj[::-1]):
        while i!=0:
            i=(int)(i/10)
        print(j)
