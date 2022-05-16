# Files
"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
filename = "dataset/mbox-short.txt"
#fsample=input("Enter the file-Nmae : ")
f=open(filename)
count=0
total=0
for line in f:
  if line.startswith('X-DSPAM-Confidence:'):
   count=count+1
   #z=line.strip()
   x=line.find("0")
   y=float(line[x:])
   print(line) 
   total=total+y
print("Count:",count ,end=" ")
print('Total:',total)
average=total/count
print("Average : ",average)