import os
os.system('clear')
class Menu(dict):
  """fill in class definition here"""
  def __init__(self):
    pass
  def dict(self,item,rate):
    self[item]=rate

class Order(Menu):
  """fill in class definition here"""
  
  def __init__(self,item,rate):
    Menu.__init__(self,item,rate)
  def display(self):
    if input=='y':
      print("Which item do u want ??")
      print()

  

class Bill:
  """fill in class definition here"""
  

m = Menu()
m['Pongal']=30
m["Idly"] = 10
m["Vada"] = 20
m['Dosa']=25
m['Lemon Rice']=30
print('Hi welcome to Hotel')
choice=input("Do u like to see the Menu y/n:")
if choice =='y':
 print("We have the following Items")
 print('Menu'.center(20,'-'))
 i=0
 for k,v in m.items():
   i+=1
   print(str(i)+'.'+k,'->',v)
 sel=int(input("Enter the index of our favourite item from above Menu : "))
 for i in m.items():
    if sel==i:
     print(f'Your selection is {m.key()}')
    
else:
  exit()


'''o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)
'''
'''b = Bill(m, o)
print(b)
'''
