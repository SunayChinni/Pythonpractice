a=5
b=2
c=9
if((a>b) & (a<c)):
    print (b)

    x=int(input("insert a number here"))
    y=float(input("insert a number here"))
    z=int(input("insert a number here"))


if ((x < y) & (x < z)):
    print(x)
elif ((y < x) & (y < z)):
    print(y)
else:
    print(z)

print(max(x,y,z), 'is a highest number')
print(min(x, y, z), 'is lowest number')