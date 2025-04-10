def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    if(y==0):
        return "Eror"
    else:
        return x/y
        
def power(x,y):
    return x**y
    
def mod(x,y):
    if(y==0):
        return "Eror"
    else:
        return x%y

if __name__ == "__main__":  
    
    print("Testing cases for math_utils functions:")  
    print("Add:", add(10, 5))  
    print("Subtract:", subtract(10, 5)) 
    print("Multiply:", multiply(10, 5))  
    print("Divide:", divide(10, 5))
    print("Divide (*by zero*):", divide(10, 0)) 
    print("Power:", power(2, 3))
    print("Mod:", mod(10, 3))   
