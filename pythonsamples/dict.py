grade={'sai':98,'hari':79,'ranga':45,'ranga':23}

for i in grade:
    print(i)


print(grade)

print(grade['hari'])

grade['siva']=95
print(grade)

del grade['ranga']
print(grade)

'''a=[1,2,3,4,,5,6 ]
b=[4,5,7,8,2,3]

dict={'a':[1,2,3,4,,5,6],'b':[4,5,7,8,2,3]}
print(dict)'''


d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

# This loop will display Keys
for x in d1:
    print(x)
print("Thanks")
print("------------------")

# display values
for x in d1:
    print(d1[x])
print("Thanks")
print("------------------")

# Program to display key and value

for x in d1:
    print(x," -- ",d1[x])
print("Thanks")
print("------------------")

# Example's on Dict Functions

# Example 1
for x in d1.items():
    print(x,type(x))
print("Thanks")
print("------------------")

# Example 2
for key,value in d1.items():
    print(key,value)
print("Thanks")
print("------------------")


d1 = {"101":[10,20,30,40,50,60],
      "102":[11,22,33,44,55,66],
      "103":[99,88,77,66,55,44]}

for key,value in d1.items():
    print("Idno = ",key,end=" ")
    print("Toal = ",sum(value))
    print("High Marks = ",max(value),end=" ")
    print("Low Marks = ",min(value))


d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

for x in d1.keys():
    print(x)

print("-----------------------")

for x in d1.values():
    print(x)

for x in range(1,4):
    for y in range(1, 5):
        print(x, end=" ")
    print()

for x in "sathya":
    print(x,end=" ")