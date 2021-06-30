import math
import numpy as np

def func( x ): 
    return ((math.e)**x / (1+x)) #<--------------------------------function
  
def simpsons_1_3_( lower_limit, upper_limit, n ): 
    a = 0
    h = ( upper_limit - lower_limit )/n 
    x = list() 
    fx = list() 
    
    while a<= n: 
        x.append(lower_limit + a * h) 
        fx.append(func(x[a])) 
        a += 1  
    res = 0
    
    b = 0
    while b<= n: 
        if b == 0 or b == n: 
            res+= fx[b] 
        elif b % 2 != 0: 
            res+= 4 * fx[b] 
        else: 
            res+= 2 * fx[b] 
        b+= 1
    res = res * (h / 3) 
    return res 
      
# Driver code 
#according to the question

x0 =0 #<---------------------lower limit
x1 =6 #<---------------------upper limit
n = 4 #<--------------------- no of interval we are assuming 4

print("%.4f"% simpsons_1_3_(x0, x1, n))

