year =int(input(' ввести год '))
if (year % 4==0)or(year % 100==0)or(year % 400==0):
    print('високосный год')
else:
    print('не високосмный год')

 