a=int(input('Ввести одну сторону треугольника = ' ))
b=int(input('Ввести вторую сторону треугольника = ' ))
c=int(input('Ввести третью сторону треугольника = '))
if(a+b>c)and(b+c>a)and(c+a>b):
    print('\nСуществует такой тругольник')
    if (a!=b and b!=c and c!=a):
        print('\nТреугольник разносторонний')
    elif ( a==b and b!=c)or(b==c and  b!=a)or(c==a and a!=b):
        print('\nТреугольник равнобедренный')
    elif (a==b and b==c and c==b):
        print('\nТреугольник равносторонний')
else:
    print('Не существует такого тругольника')
    