
name=input("enter name")
print(name * 10)
print((name+"\n") * 10)
print((input("enter name")+"\n")*10)

# program to read name and number of times from user
name=((input("enter names")+"\n")*int(input("number of times from user")))
print(name)

#string length
namestr=input("enter string")
print(len(namestr))


no=int(input("enter no"))
if(no>0):
    print(no,"is positive")
else:
    if(no<0):
       print(no,"is negative")

a = int(input("enter a number here"))
if (a % 2 == 0):
     print("even num")

else:
    if(a%2!=0):
      print("odd num")

a=int(input("enter 1no"))
b=int(input("enter 2no"))
c=int(input("enter 3no"))
if(a>b and a>c):
    largest = a
elif(b>c and b>a):
    largest = b
elif(c>a and c>b):
    largest = c

print("The largest number between", a, ",", b, "and", c, "is", largest)
