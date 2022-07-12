print(" Menu List ".center(40,'*'))
print('_'*34)
class Menu():
  """fill in class definition here"""
  def __init__(self,item,rate):
    self.item=item
    self.rate=rate

  def show(self):
    print(f" Item is :'{self.item}' ,rate = '{ self.rate}'  ")

idly=Menu("Idly",'20')
vada=Menu("Vada",'10')
dosa=Menu("Dosa",'25')
poori=Menu("Poori",'30')

poori.show()
idly.show()
vada.show()
dosa.show()

