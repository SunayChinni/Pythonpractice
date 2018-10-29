open(r"C:\Users\Externet\Desktop\python\cls1.txt").read()

ts=open(r"C:\Users\Externet\Desktop\python\pych.txt",'w')
ts.write("hii welcom")
ts.close()


def fun1():

    return 10, True, 10.25, "Ravi"

a = fun1()
print(a)
print(type(a))
