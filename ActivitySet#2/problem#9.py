class Menu(dict):
  """fill in class definition here"""
  def __init__(item,rate):
    self.item=item
    self.rate=rate

class Order:
  """fill in class definition here"""
  

class Bill:
  """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
