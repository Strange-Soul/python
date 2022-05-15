# Functions

"""
 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. """

hrs = float(input("Enter hours? "))
rt = float(input("Enter rate per hour? "))
def computepay(h,r):
    if h>40:
      pay=h*r
      ot=(h-40)*(r*0.5)
      grasspay=pay+ot
      print("Pay : ",grasspay)
    else:
      pay=h*r
      print("Pay : ",pay)
    print("Done !!!")
    return 'pay'



p = computepay(hrs, rt)
print("Pay",p)

# Loops & Iterators

"""
 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""
"""
largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break

    # ...

    print(num)

print("Maximum", largest)
"""
smallest=None
largest=None
#b=list()
while True:
  num=input("Enter a number : ")
  if num == 'done':
    break
  else:
   try:
     n=int(num) 
     #b.append(n)
     if largest==None:
       largest=n
     if n>largest:
        largest=n
     if smallest==None:
        smallest=n
     if n<smallest:
        smallest=n
   except:
     print("Invalid Input \n Error \n Re-enter the number")
"""largest=max(b)
largest=min(b)"""
print('Largest: ',largest)
print('smallest: ',smallest)


    