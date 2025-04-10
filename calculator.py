
import math_utils


def main():  
    print("Welcome to the simple calculator!")  
    num1 = float(input("Enter first number: "))  
    num2 = float(input("Enter second number: "))  
    operator = input("Enter operator (+, -, *, /, **, %): ")  

    operations = {  
        '+': math_utils.add,  
        '-': math_utils.subtract,  
        '*': math_utils.multiply,  
        '/': math_utils.divide,  
        '**': math_utils.power,  
        '%': math_utils.mod  
    }  
 
    if operator in operations:  
        result = operations[operator](num1,num2)  
        print(f"The result of {num1} {operator} {num2} is: {result}")  
    else:  
        print("Error: Invalid operator.")  

if __name__ == "__main__":  
    main()  
