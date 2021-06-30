def f(x,y):
    return -2*x-y #<----------------------------------function

def rk4(x0,y0,xn,n):

    h = (xn-x0)/n

    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        y0 = yn
        x0 = x0+h
    
    print(xn,"\t",yn)

# Inputs

x0 = float(input('initial value of x0 :-> '))
y0 = float(input('initial value of x0 :-> '))


xn = float(input('Enter xn point :-> '))

step = int(input('Number of steps :-> '))

# RK4 method call
rk4(x0,y0,xn,step)