# Conditional Execution
hours = input("Enter hours? ")
hr=float(hours)
rate=input("Enter the rate per hour? ")
rt=float(rate)
if hr > 40:
   pay=hr*rt
   final_rt=(hr-40)*(rt*0.5)
   grass_pay=pay+final_rt
   print('Pay:',grass_pay)
else:
  pay=hr*rt
  print(pay)
print("Done !")


