def tra():
    N=[1]
    while True:
        yield N
        N.append(0)
        N=[N[i]+N[i-1] for i in range(len(N))]
        
def print_tra(x):
    a=0
    for t in tra():
        t1=str(t)
        t2=t1.replace('[',' ').replace(',',' ').replace(']',' ')
        print(t2)
        a+=1
        if a==x:
            break
n=int(input())
print_tra(n)
