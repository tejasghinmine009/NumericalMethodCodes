def func( x ): 
    return x * x * x -3* x  -5 #<---------------------------normal function
  

def deriv_Func( x ): 
    return 3 * x * x - 3  #<------------------------------derivative function
  

def newtonRaphson( x ): 
    h = func(x) / deriv_Func(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/deriv_Func(x)    
        x = x - h   
    return x 
  
# Driver program to test above 
x0 = int(input(" Initial value of x :-> "))
print(newtonRaphson(x0))