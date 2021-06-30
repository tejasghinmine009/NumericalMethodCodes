def func(x,y):
    return(x*x*y -1)                   #<------------------------------function

def taylor_series(x,y,step,itter):
    x_final = x+step
    y_final = 0
    h = step
    while(itter > 0):
        yl = func(x,y)
        yll = 2*x*y +x*x*yl
        ylll = 2*y+4*x*yl+x*x*yll
        yllll = 6*yl+6*x*yll+x*x*ylll
        y_final = y+h*yl+(((h**2) * yll )/ 2 )+(((h**3) *ylll )/(3*2))+(((h**4) *yllll )/(4*3*2))
        x = x_final
        y = y_final
        itter = itter-1
    return y_final
    
x0 = float(input("intial value of x :-> "))
y0 = float(input("intial value of y :-> "))
step_size = float(input("enter step size :-> "))
itter = int(input("no of itteration :-> "))

print(taylor_series(x0,y0,step_size,itter))
