

a=100
def fun1():
    print("hi")
    print(a)

def fun2():
    print(a)
    print("hell")

a=10
print(a)
fun2()
print(a)
fun1()
print(a)
print("----")

def fun3():
    print("hiss")
    print(b)
b=13
def fun4():
    print(b)
    print("hall")
b=11

fun4()
fun3()
print("----")

a=1000
def fun5():
    global a
    a=50
    print(a)

print(a)
fun5()
print(a)
'''def func1():
    global a
    a=50
    print(a)

print(a)  #error
fun5()
print(a)''' #50

a = 100
def fun1():
    global a
    a = 50
    print(a)

print(a)
fun1()
print(a)



a = 100
def fun1(i,j):
    print(i+a)
    print(j+a)
def fun2():
    global a
    a = 1000
    print(a)
def fun3():
    global b
    b = 100
    return a+b


fun1(10,20)
fun2()
print("---")
res=fun3()
print(res)