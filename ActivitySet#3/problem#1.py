class point:
  
  def __init__(self):
    self.x=[]
    self.y=[]
  def __setitem__(self):
    n=int(input("Enter the Number of co-ordinates: "))
   
    for i in range(1,n+1):
       x=float(input(f"Enter the {i}'x'co-ordinate:"))
       y=float(input(f"Enter the {i} 'y' co-ordinate:"))
       self.x.append(x)
       self.y.append(y)
       i+=1
    #print(self.x,self.y)
class Rectangle(point):
  def __init__(self):
    super().__init__
    self.dist=0
  def cal_dist(self):
    
    self.dist1=math.sqrt((pt.x[1]-pt.x[0])**2-(pt.y[1]-pt.y[0])**2)
    self.dist2=math.sqt((pt.x[2]-pt.x[1])**2-(pt.y[2]-pt.y[1])**2)
    self.dist3=math.sqrt((pt.x[2]-pt.x[0])**2-(pt.y[2]-pt.y[0])**2)
    print('Dis-1:',self.dist1,'Dist-2:',self.dist2,'Dist3:',self.dist3)
  def __gt__(self):
    if self.dist1> self.dist2  & self.dist1>self.dist3:
      self.dist=self.dist2*self.dist3
    elif self.dist2> self.dist1 & self.dist2>self.dist3:
      self.dist=self.dist1*self.dist3
    else:
      self.dist=self.dist1*self.dist2
   
    #return (self.dist2*self.dist3 if self.dist1> self.dist2 and self.dist1>self.dist3  else self.dist1*self.dist3  )
      
x,y=[],[]
pt=point()
pt.__setitem__()
print("X co-ordinate:",pt.x)
print("Y co-ordinates:",pt.y)
x_y=[(x,y) for x,y in zip(pt.x,pt.y)]
print(tuple(x_y))
#x_y=[i+j for i,j in (pt.)]
rt=Rectangle()
print(rt.cal_dist())



