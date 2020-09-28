b1=int(input('первый член'))
q=int(input('множитель'))
n=int(input('член'))
for i in range (1,n,1):
    b=b1*q**(i)
    print(b,end =' ')