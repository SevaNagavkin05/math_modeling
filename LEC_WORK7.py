a=int(input('Введите число а '))
b=int(input('Введите число в '))
c=int(input('Введите число с '))     
DIS=b**2-4*a*c
if DIS<0:
    print('Нет действительных корней')
elif DIS>0: 
    x1=(-b+DIS**(0.5))/(2*a)
    x2=(-b+DIS**(0.5))/(2*a)
    print('Два различных корня',x1,x2)
if DIS==0:
    print('Один корень',x1)    
