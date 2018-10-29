l1 = [10,20,30,40,50]
print(l1)
print(l1[0])
print(l1[-1])
l1[2] = 90
print(l1)

l1 = [10,20,30]
# l2 = l1+3 Error
# TypeError: can only concatenate list (not "int")
# print(l2)

l2 = [40,50,60]
l3 = l1+l2
print(l1)
print(l2)
print(l3)
print("-------------------------")

l1 = [10,20,30]
l2 = [1,2,3]
# l3 = l1*l2 # Error
# TypeError: can't multiply sequence by non-int of type 'list'
# print(l3)

l3 = l1*3
print(l3)

l1 = [10,20,30,40,50,60,70,80,90,100]
print(l1[0:3])
print(l1[0:5:2])
print(l1[0:10:3])
print(l1[-1:-11:-2])

l1 = [] # Empty List
print(l1)
s1 = int(input("Enter 1sub Marks"))
l1.append(s1)
s2 = int(input("Enter 2sub Marks"))
l1.append(s2)
s3 = int(input("Enter 3sub Marks"))
l1.append(s3)
print("Marks = ",l1)
print("Total marks = ",sum(l1))

first = [11,12,13,14,15,16,17]
second = [10,20,30,40,50]

# adding second list elements to first list
first.extend(second)

print(first)
print(second)


l1 = [10,20,30]
print(l1)
val = l1.pop(0)
print("Removed value = ",val)
print(l1)

l1 = [10,20,30,40,50,10,50,60,30]
no = l1.index(30)
print(no)


t1 = (10,"Ravi",10.25,False)
t2 = (20,"Kumar",20.25,True)
t3 = t1+t2
print(t3)

t4 = t1*2
print(t4)

t1 = (10,"Ravi",10.25,False)
print(t1[0:2])
print(t1[0:5:2])


t1 = (10,20,"Ravi",40.85,10,30,20,10)
coun = t1.count(10)
print(coun)

ind = t1.index("Ravi")
print(ind)