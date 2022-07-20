"""Problem 1: Rectangle Area
Develop a program that, given as input the cartesian coordinates of three vertices of a rectangle,
reports the area of that rectangle. You will recall that the area of a rectangle is the product of
the lengths of any two adjacent sides.
Input: The first line contains a positive integer n indicating how many rectangles are to be
analyzed. Each rectangle is described on a single line via six real numbers, x1, y1, x2, y2, x3,
and y3, separated by spaces. These provide the coordinates of three of the rectangle’s vertices,
namely P1(x1, y1), P2(x2, y2), and P3(x3, y3).
Output: For each rectangle provided as input, report its area.
Sample input
------------
3
0.0 0.0 0.0 1.0 1.0 0.0
-1.0 2.0 3.0 5.0 1.0 1.0
5.0 9.0 -0.5 0.0 7.5 5.0
Resultant output
----------------
Area of rectangle with vertices (0.0,0.0),(0.0,1.0),(1.0,0.0) is 1.0
Area of rectangle with vertices (-1.0,2.0),(3.0,5.0),(1.0,1.0) is 10.0
Area of rectangle with vertices (5.0,9.0),(-0.5,0.0),(7.5,5.0) is 44.5 """
import math

def distance(x,X,y,Y):
  dist=math.sqrt( ((X-x)**2) - ((Y-y)**2))
  return dist
def main():
 x1,x2,x3,y1,y2,y3=input("x1:"),input("x2:"),input("x3:"),input("y1:"),input("y2:"),input("y3:")
 x1,x2,x3=float(x1),float(x2),float(x3)
 y1,y2,y3=float(y1),float(y2),float(y3)

 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f) is " %(x1,y1,x2,y2),distance(x1,x2,y1,y2))
 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f)is "%(x2,y2,x3,y3),distance(x2,x3,y2,y3))
 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f) is "%(x3,y3,x1,y1),distance(x3,x1,y3,y1))
    
main()