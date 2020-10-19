import numpy as np 
my_array1=np.zeros((3,3))
for i, x in np.ndenumerate(my_array1):
    my_array1[i]=input(f'{i}')
    print(my_array1[i])

my_array2=np.zeros((3,3))
my_array3=np.zeros((3,3)) 
for(i,j)  in np.ndenumerate(my_array2):
    my_array2[i]=input(f'{i}')
    if (my_array1[i]>=my_array2[i]):
        my_array3[i]=my_array1[i]
    else:   
        my_array3[i]=my_array2[i]
        
print(my_array3)    
    
    
    
    
    

    