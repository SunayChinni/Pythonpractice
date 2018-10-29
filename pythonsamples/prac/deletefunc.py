'''def fun1():
    print("hii")
    print("function")

fun1()
del fun1
print("function is deleted")
fun1'''

def fun1():
    print("hii")
    print("function")

fun1()
a=fun1
del fun1
print("function is deleted")
a()

def add():
    sub()
    print("I am Add")

def mul():
    sub()
    print("I am Mul")

def sub():
    print("I am Sub")

def div():
    add()
    print("I am Div")

print("Hi")
div()
print("Bye")