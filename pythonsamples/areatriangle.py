a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2
print(s)
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

q= (b**2)-(4*a*c)
print(q)

x=10
y=23
#swap
temp=x
x=y
y=temp
print(x)
print(y)