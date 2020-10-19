import numpy as np

l=int(input('введите длину масива:'))
h=int(input('введитеширину массив:'))

array1=np.zeros((h,l))

array2=np.zeros((l,h))
for (i,j), x in np.ndenumerate(array1):
    num=int(input(f'[{i},{j}]'))
    array1[(i,j)]=num
    array2[(j,i)]=num
    
array3=np.zeros(l)
for i,x in np.ndenumerate(array3):
    array3[i]=array2[i].max()
print(array3)    