class Menu(dict):
  def __init__(self):
    pass
  def dict(self,item,rate):
    self[item]=rate
    
menu=Menu()
menu['Idly']=20
menu['Dosa']=25
menu['Vada']=10
m.dict()