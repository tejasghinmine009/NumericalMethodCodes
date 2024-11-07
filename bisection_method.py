itter= int(input("Maximum no of itteration :-> "))
def func(x): 
    return x*x*x - x -1  #<------------------------------function
   
def bisection(a,b): 
    if (func(a) * func(b) >= 0): 
        print("You have not assumed right a and b\n") 
        return
 
    c = a 
    for i in range(itter): 
        c = (a+b)/2
        if (func(c) == 0.0): 
            break
        if (func(c)*func(a) < 0): 
            b = c 
        else: 
            a = c          
    return c
      
# Driver code 

a = int(input("enter lower inital value :-> "))
b = int(input("enter upper intial value :-> "))
print()
print(bisection(a, b))
