import numpy as np

def func( x ): 
    return (3*x**2 *(np.exp(x**3))) #<--------------------------------function
   

def simpson_3_8_(ll, ul, il):  
     
    interval_size = (float(ul - ll) / (il-1)) 
    sum = func(ll) + func(ul); 

    for i in range(1, il): 
        if (i % 3 == 0): 
            sum = sum + 2 * func(ll + i * interval_size) 
        else: 
            sum = sum + 3 * func(ll + i * interval_size) 
    return ((float( 3 * interval_size) / 8 ) * sum ) 
  
# driver function 
x0 =0
x1 =1
n =21
  
print(simpson_3_8_(x0, x1, n))

