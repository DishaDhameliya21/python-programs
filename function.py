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
