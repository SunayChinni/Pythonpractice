def fun1():
    a=20
    print(a)

fun1()

def fun1(no1,no2):
    a=no1
    b=no2
    c=a+b
    print(c)
    print(no1+no2)

fun1(10,20)

def calc():
    a=10
    b=20
    c=b-a


    return c
calc() #empty
print(calc())
res=calc()
print(res)


def calci(no1,no2):
    a=no1
    b=no2
   

    return a+b

print(calci(10,20))
res=calci(11,20)
print(res)




def div(no1,no2):
    return (no1+no2)
def mul(no1,no2):
    print("The sum = ",div(no1,no2))
    return no1-no2
def sub(no1,no2):
    print("The sub = ",mul(no1, no2))
    return no1*no2
def add(no1,no2):
    print("The Mul = ",sub(no1,no2))
    return no1/no2

a = int(input("1st No : "))
b = int(input("2nd No : "))
print("The Div = ",add(a,b))