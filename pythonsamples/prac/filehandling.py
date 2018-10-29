
print(open("fors.py","r").read())

f=open("fors.py")
s=f.read()
print(s)
print("---------")

f=open("fors.py")
s1=f.read(15)
print(s1)

p=open(r"C:\Users\Externet\Desktop\python\if.py","r")
s=p.read()
print(s)

try:
 p=open(r"C:\Users\Externet\Desktop\python\ifS.py","r")
 t=p.read()
 print(t)
except FileNotFoundError as fnf:
 print(fnf)

print(len(open("fors.py").read()))

f=open("fors.py")
for x in f:
     print(x)

print(len(open("testshel.py","r").readlines()))

print(len(open("testshel.py").readlines()))

with open("input.py","r") as f:
 s=f.read()
 print(s)
