def y( x ): 
    return (1/x) #<---------------------------function
      
def trapezoidal (a, b, n): 
    h = (b - a) / n       
    s = (y(a) + y(b)) 
    i = 1
    while i < n: 
        s += 2 * y(a + i * h) 
        i += 1
    return ((h / 2) * s) 
  

x0 = int(input("lower limit :-> "))
xn = int(input("Upper Limit :-> "))
  
n = int(input("interval length "))
print (trapezoidal(x0, xn, n)) 
  
  