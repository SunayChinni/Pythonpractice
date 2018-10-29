a=10
def fun1():
    print("fun1")
    print(a)

def fun2():
        print("fun2")


def fun3():
    a=5

    print("fun3")
    print(a)

print(a)
fun2()
fun3()
fun1()



def fun4():
    print("fun4")
    fun5()



def fun5():
        print("fun5")
        fun6()

def fun6():

    print("fun6")


fun4()
fun6()
fun5()

