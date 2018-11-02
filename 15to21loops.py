#15 Print Sathya Technologies for 10 times
for i in range(1,11):
    print("sathya",end=" ")

#16. Print 1  to  10   numbers
for i in range(1,11):
    print(i,end=" ")

#17.Print even numbers from 1 to 10
for x in range(1, 10):
    if (x % 2 == 0):
        print(x,end=" ")

#18.Print odd numbers from 1 to 10
for x in range(1, 101):
    if (x % 2 != 0):
        print(x,end=" ")

#19.Print sum of all the numbers  1 to 10
for num in range(1,11):
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print(sum,end="")


#20.Print sum of all even numbers from 1 to 10

n=int(input('Enter the limit '))
i=1
sum=0
while i<n:
    if i%2==0:
        sum=sum+i
    i=i+1
print ("sum of even numbers",sum)

#21.Print sum of all odd numbers from 1 to 10

n=int(input('Enter the limit '))
i=1
sum=0
while i<n:
    if i%2!=0:
        sum=sum+i
    i=i+1
print ("sum of even numbers",sum)'''

