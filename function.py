#simple print helo world using function
def printhello():
    print("Hello World !!")

printhello()    

#function with parameters
def add(a , b):
    ans = a + b
    print(ans)

add(5 , 7)    

#function with defualt parameter 
def greet(name = "Disha"):
    print(f"Hello ,{name}!")

greet() 

greet("Priya")   

#Function with Variable Number of Arguments (*args and **kwargs)
def print_number(*args):
    for i in args:
        print(i)

print_number(1 , 2, 3, 4, 5)


def print_info(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_info(name = "Disha" , age = 20 , sex = "female")       

#function with return value
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  
print(is_even(7))  


#function with multiple arguments
def name(fname):
    print(fname , "Dhameliya")

name("Krina")
name("Janvi")
name("Ved")
name("Vrund")    


#function to make calculater
def add(x , y):
    return x + y
def multiply(x , y):
    return x * y
def substract(x , y):
    return x - y
def division(x , y):
    if(y == o):
        return "cannot divide by zero"
    return x / y

print("select operation")
print("1.addition:")
print("2.multiplication:")
print("3.substraction:")
print("4.division:")

choice = input("Enter your choice (1,2,3,4):")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if choice == '1':
    print(f" The result is :{add(num1 , num2)}")
elif choice == '2':
    print(f"The result is : {multiply(num1 , num2)}")    
elif choice == '3':
    print(f"The result is : {substract(num1 , num2)}")    
elif choice == '4':
    print(f"The result is : {division(num1 , num2)}")   

else:
    print("Invalid input")     
    

