a=int(input())
e=[]

for i in range(a):
    b=input()
    c=int(b,16)
    d=oct(c)
    f=str(d)
    h=int(f[2::])
    e.append(h)
for j in range(0,a):
    print(e[j])
