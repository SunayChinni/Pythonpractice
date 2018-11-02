'''#22. Find the factorial of a given number

num=int(input("enter a given number"))
factorial=1
if num<0:
    print("enter a positive number")
elif num==0:
    print("the factorial of 0 is 1")
else:
   for i in range(1,num+1):
       factorial=factorial*i
print(factorial)

#23.WAP to Check the number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#24.Print the number from  10 to 1
for i in range(10,0,-1):
    print(i,end=" ")'''

#25.Input any 10 numbers find out no of even numbers and no of odd numbers

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
