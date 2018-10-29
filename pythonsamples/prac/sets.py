s1 = {10,20,30,10,40}
print(s1)
# print(s1[0]) #  'set' object does not support indexing
# print(s1[0:2]) # 'set' object is not subscriptable
s2 = {5,6,7,8,9}
print(s2)
# s3 = s1+s2 Error
# print(s3)

# s3 = s1 * 2
# print(s3)


l1 = [] # Empty List
print(type(l1))

t1 = () # Empty Tuple
print(type(t1))

s1 = {} # Empty dict
print(type(s1))


d1 = {}
print(d1)
print(type(d1))
print("------------------")

# Holding 1 Employee Details
d1 = {
    "idno":101,
    "name":"Ravi",
    "salary":125000.00,
    "Designation":"Developer"
    }
print(d1)

print("------------------")

d1 = {
    "idno":101,
    "name":"Ravi",
    "salary":125000.00,
    "Designation":"Developer"
    }
print(d1["salary"])
print(d1["Designation"])
d1["cost"] = 185000.00
print(d1)

