class Menu(dict):
  """fill in class definition here"""
  def __init__(self):
    pass
  def dict(self,item,rate):
    self[item]=rate

class Order(Menu):
  """fill in class definition here"""
  
  def __init__(self,item,qty):
   Menu.__init__(item)
   
   self.qty=0
   
  def dict(self,item,qty):
    self[item]=qty

class Bill(Order):
  """fill in class definition here"""
  def __init__(self,item,rate,qty):
    #Menu.__init(self,item,rate)
    Order.__init__(self,item,qty)
  def selection(self):
    print(f"U selected {self.qty}->{self.item}")
m = Menu()
m['Pongal']=30
m["Idly"] = 10
m["Vada"] = 20
m['Dosa']=25
m['Lemon Rice']=30
m['Tea']=8
print('Hi welcome to Hotel')
choice=input("Do u like to see the Menu y/n:")
if choice =='y':
 print("We have the following Items")
 print('Menu'.center(20,'-'))
 i=0
 for k,v in m.items():
   i+=1
   print(str(i)+'.'+k,'->',v)
    
else:
  exit()

print("Accepting your Order")
o = Order()
try:
    o["vada"] = 2
    o["pongal"] = 2
  
except KeyError as e:
    print(e)
print(f"U selected {o.qty}->{o.item} ")

b = Bill(m, o)
b=o.qty*m.rate
print(b)

