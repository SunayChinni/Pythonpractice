def display(idno,name=None,salary=0.0):

    print(idno,name,salary)
    print("idno=",idno)
    print("name=",name)
    print("salary=",salary)

#display()
display(101)
display(125.0)
display(101,"sai",123.5)
display("suma",1)
display(name="ravi",salary="125.0",idno="4")
#argument length
def show(*no1):
    for x in no1:
        print(x,end="  ")
        print()

show(10)
show(10,20)
show(10,20,30)
show(10,20,30,50)

print(10)
print(10,20)
print(10,20,30)
print(10,20,30,50)




