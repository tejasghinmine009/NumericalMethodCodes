def func( x, y ): 
    return (-2*x - y)             #<----------------------------function
      
def euler( x0, y, h, x ):
    while x0 < x: 
        y = y + h * func(x0, y) 
        x0 = x0 + h 
    return y
      


x0 = float(input("Enter intial value of x (i.e x0) :-> "))
y0 =float(input("Enter intial value of y (i.e y0) :-> "))
h =float(input("Enter step length :-> "))
x = float(input("Enter final value of x :-> "))
print()
print(euler(x0, y0, h, x)) 