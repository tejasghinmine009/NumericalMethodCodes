itter= int(input("Maximum no of itteration :-> "))

def func( x ): 
    return (x * x * x - 48)  #<--------------------------function

def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1      
    c = a       
    for i in range(itter): 
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
        if func(c) == 0: 
            break

        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
    return c
  

# Initial values assumed 
a =int(input("enetr lower limit :-> "))
b = int(input("enetr upper limit :-> "))
print()
print(regulaFalsi(a, b) )
  