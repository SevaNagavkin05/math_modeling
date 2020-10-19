import numpy as np
 
my_array1=np.zeros(5)
for i, x in np.ndenumerate(my_array1):
    my_array1[i]=input(f'{i}')
    if (i==(3,)):
        break
print(my_array1)    

volue=int(input('Введите число'))
index=int(input('Введите индекс'))

my_array2=np.insert(my_array1,volue,index)
my_array2.resize(5)
print(my_array2)  