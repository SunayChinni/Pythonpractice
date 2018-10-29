print("hello world"*10);
open(r"C:\Users\Externet\Desktop\python\cls1.txt").read();

list1=[1,2,3,3,2,4,6,6]
print(set(list1))

tens=[(20,60),(10,40),(20,30)]
a=sorted(tens)
print(a)
print(a[1])
print(tens[1])


t1 = (10,"Ravi",10.25,False)
print(t1[0:2])
print(t1[0:5:2])

a = 100
def fun1(i,j):
    print(i+a)
    print(j+a)
def fun2():
    global a
    a = 1000
    print(a)

a = 100
def fun3():
    global b
    b = 100
    return (a+b)

fun1(10,20)
fun2()
res=fun3()
print(res)

a = 100
def fun1():
    a = 50
    print(a)

print(a)
fun1()
print(a)

a = 100
def fun1():
   global a
   a = 50
   print(a)

print(a)
fun1()
print(a)


import webbrowser
web_name = input("Enter Website : ")
webbrowser.open(web_name)
