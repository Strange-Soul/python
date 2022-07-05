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
"""smallest=None
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

print('Largest: ',largest)
print('smallest: ',smallest)"""

largest=None
smallest=None
while True:
  number=input('Enter the number:')
  if number == 'done':
    break
  try:
    num=float(number)
    if largest == None or num >largest:
     largest=num
    if smallest == None or num < smallest:
     smallest=num
  except:
    print("Re-enter the number \n Error")
print('Maximum is :',largest)
print('Minimum is :',smallest)
    
 
  
