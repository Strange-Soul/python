print("\033[1m Menu List \033[0m")
class Menu():
  """fill in class definition here"""
  def __init__(self,item,rate):
    self.item=item
    self.rate=rate

  def show(self):
    print(f" Item is :\033[1m '{self.item}' \033[0m,rate = \033[1m '{ self.rate}' \033[0m ")

idly=Menu("Idly",'20')
vada=Menu("Vada",'10')
dosa=Menu("Dosa",'25')
poori=Menu("Poori",'30')

poori.show()
idly.show()
vada.show()
dosa.show()

