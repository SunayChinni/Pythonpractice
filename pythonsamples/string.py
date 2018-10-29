a='hello'
b="practICe"
d="welcome python"
c=55
print(a)
print(b)
print(a+b)
print(a,c)
print(a,b)
print(a+str(c))

print(a.upper())
print(b.lower())
print(len(d))
print(d[5])
print(d[:5])
print(b[2:5])
print(d[5:14])
print()


s1 = "SatHyA"
s2 = s1.swapcase()
print(s1)
print(s2)
print("----------------------")
s1 = "this is sathya from ampt"
s2 = s1.title()
print(s1)
print(s2)
print("----------------------")
s1 = "this is sathya. from ampt"
s2 = s1.capitalize()
print(s1)
print(s2)

s1 = "Hello this is naveen from sathya tech ampt hyd"
va = s1.split()
print(va)

va = s1.split('a')
print(va)

s1 = input("Enter a String : ")
res = s1.split()
print(res)
print("The Total Words = ",len(res))
print("The Total char's = ",len(s1))