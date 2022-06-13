# Files
"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
"""filename="dataset/mbox-short.txt"
fhandle=open(filename)
count=0
total=0
for line in fhandle:
  if line.startswith("X-DSPAM-Confidence:"):
     s=line.split()
     v=float(s[1])
     count+=1
     total+=v
print("count",count,"Total",total)
average=total/count
print("Average:",average)"""

file_name="dataset/mbox-short.txt"
file_open=open(file_name)
count=0
total=0
l=list()
for line in file_open:
  if line.startswith("X-DSPAM-Confidence:"):
    line=line.rstrip().split()
    num=float(line[1])
    l.append(num)
    count+=1
    total+=num
print("Numbers in th file as fallows:")
print(l)
print("Count:",count,"Total:",total)
print("Average:",total/count)
   
