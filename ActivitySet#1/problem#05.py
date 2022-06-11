#conditional execution
"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""

"""marks=input("Enter the Score > ")
score=float(marks)
if (score<0.0) or (score>1.0):
    print("Out of Range ")
    print('Error')
elif (score >= 0.0) and (score <= 1.0):
    print("Score is valid for printing Grade")
    if(score >= 0.9):
       print("A")
    elif(score >= 0.8):
      print("B")
    elif(score >= 0.7):
      print("C")
    elif(score >= 0.6):
      print("D")
    elif (score < 0.6):
      print("F")
else:
 print("All are done")"""
mark=input('Enter the score:')
try:
  marks=float(mark)
except:
  print("Invalid character \n Re_enter the digit !!!")
  
if marks >1.0 or marks <0.0:
  print("Out of range!!")
elif marks>0.0 and marks<1.0:
  print("Calculating the Grade..... \n please wait for a moment!!!")
  if marks>=0.9:
    print("Grade:'A'")
  elif marks>=0.8:
    print("Grade:'B'")
  elif marks>=0.7:
    print("Grade:'C'")
  elif marks>=0.6:
    print("Grade:'D'")
  elif marks<0.6:
    print("Grade:'F'")
else:
  print("All Done !!!")