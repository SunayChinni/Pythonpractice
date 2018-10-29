
x=9
if(x%2 ==0):
    print("even num")
else:
    print("odd num")



a=int(input("enter a number here"))
if (a%2 == 0):
        print("even num")

else:
        print("odd num")

year = 2000

        # To get year (integer input) from the user
        # year = int(input("Enter a year: "))

if (year % 4) == 0:

     print("{0} is a leap year".format(year))

num = 7
factorial = 1
if(num<0):
    print("negative")
else:
  for i in range(1, num + 1):
    factorial = factorial * i

    print(factorial)